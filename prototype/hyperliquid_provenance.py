"""Analyse déterministe de provenance et de fraîcheur Hyperliquid."""
from dataclasses import dataclass
from datetime import datetime, timezone
from decimal import Decimal
import unittest

@dataclass(frozen=True)
class Observation:
    metric: str
    source: str
    observed_at: str
    unit: str
    value: Decimal

def age_seconds(observation: Observation, now: datetime) -> int:
    """Âge signé en secondes : négatif si l'observation est datée dans le futur."""
    observed=datetime.fromisoformat(observation.observed_at.replace("Z","+00:00"))
    if observed.tzinfo is None:
        raise ValueError("observed_at must include a timezone")
    return int((now-observed).total_seconds())

def is_fresh(observation: Observation, now: datetime, max_age_seconds: int, max_clock_skew_seconds: int = 5) -> bool:
    # Une date future au-delà de la tolérance d'horloge n'est pas « fraîche » :
    # sans ce contrôle, une source mal horodatée resterait valide indéfiniment.
    age=age_seconds(observation,now)
    return bool(observation.source and observation.unit) and -max_clock_skew_seconds<=age<=max_age_seconds

class ProvenanceTests(unittest.TestCase):
    def test_fresh_observation_requires_source_and_unit(self):
        now=datetime(2026,1,1,12,tzinfo=timezone.utc)
        obs=Observation("mark_price","node-1","2026-01-01T11:59:30Z","USD",Decimal("101.25"))
        self.assertTrue(is_fresh(obs,now,60))
    def test_missing_provenance_is_rejected(self):
        now=datetime(2026,1,1,12,tzinfo=timezone.utc)
        obs=Observation("volume","","2026-01-01T11:59:30Z","",Decimal("1"))
        self.assertFalse(is_fresh(obs,now,60))

    def test_future_observation_is_rejected(self):
        now=datetime(2026,1,1,12,tzinfo=timezone.utc)
        obs=Observation("mark_price","node-1","2026-01-01T13:00:00Z","USD",Decimal("101.25"))
        self.assertFalse(is_fresh(obs,now,60))
    def test_small_clock_skew_is_tolerated(self):
        now=datetime(2026,1,1,12,tzinfo=timezone.utc)
        obs=Observation("mark_price","node-1","2026-01-01T12:00:03Z","USD",Decimal("101.25"))
        self.assertTrue(is_fresh(obs,now,60))
    def test_naive_timestamp_is_rejected(self):
        now=datetime(2026,1,1,12,tzinfo=timezone.utc)
        obs=Observation("mark_price","node-1","2026-01-01T11:59:30","USD",Decimal("1"))
        with self.assertRaises(ValueError): is_fresh(obs,now,60)

if __name__=="__main__": unittest.main()
