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
    observed=datetime.fromisoformat(observation.observed_at.replace("Z","+00:00"))
    return max(0,int((now-observed).total_seconds()))

def is_fresh(observation: Observation, now: datetime, max_age_seconds: int) -> bool:
    return bool(observation.source and observation.unit) and age_seconds(observation,now)<=max_age_seconds

class ProvenanceTests(unittest.TestCase):
    def test_fresh_observation_requires_source_and_unit(self):
        now=datetime(2026,1,1,12,tzinfo=timezone.utc)
        obs=Observation("mark_price","node-1","2026-01-01T11:59:30Z","USD",Decimal("101.25"))
        self.assertTrue(is_fresh(obs,now,60))
    def test_missing_provenance_is_rejected(self):
        now=datetime(2026,1,1,12,tzinfo=timezone.utc)
        obs=Observation("volume","","2026-01-01T11:59:30Z","",Decimal("1"))
        self.assertFalse(is_fresh(obs,now,60))

if __name__=="__main__": unittest.main()
