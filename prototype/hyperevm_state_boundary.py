"""Modèle explicite de frontière EVM / HyperCore."""
from dataclasses import dataclass
import unittest

@dataclass(frozen=True)
class StateEvent:
    layer: str
    action: str
    block: int
    finalized: bool

VALID_LAYERS = {"evm", "hypercore", "bridge"}

def is_consistent(event: StateEvent) -> bool:
    return event.layer in VALID_LAYERS and event.block >= 0 and bool(event.action)

def reaches_finality(events, block: int) -> bool:
    return any(e.block == block and e.layer == "bridge" and e.finalized for e in events)

class StateBoundaryTests(unittest.TestCase):
    def test_evm_submission_is_not_bridge_finality(self):
        events = [StateEvent("evm", "submit_order", 42, False)]
        self.assertFalse(reaches_finality(events, 42))
    def test_bridge_finality_is_explicit(self):
        events = [StateEvent("evm", "submit_order", 42, False), StateEvent("bridge", "finalize_withdrawal", 42, True)]
        self.assertTrue(reaches_finality(events, 42))
    def test_unknown_layer_is_rejected(self):
        self.assertFalse(is_consistent(StateEvent("unknown", "x", 1, False)))

if __name__ == "__main__":
    unittest.main()
