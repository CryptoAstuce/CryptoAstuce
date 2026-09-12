"""Arithmétisation minimale d'une trace STARK."""
from dataclasses import dataclass
import unittest

@dataclass(frozen=True)
class TraceRow:
    step: int
    value: int

def valid_trace(rows, modulus: int) -> bool:
    return bool(rows) and all(row.step == i and 0 <= row.value < modulus for i, row in enumerate(rows))

def transition_ok(rows, delta: int, modulus: int) -> bool:
    return valid_trace(rows, modulus) and all((b.value-a.value-delta) % modulus == 0 for a,b in zip(rows, rows[1:]))

class TraceTests(unittest.TestCase):
    def test_valid_transition(self):
        self.assertTrue(transition_ok([TraceRow(0,2),TraceRow(1,5),TraceRow(2,8)],3,17))
    def test_bad_transition_is_rejected(self):
        self.assertFalse(transition_ok([TraceRow(0,2),TraceRow(1,6)],3,17))
    def test_non_canonical_step_is_rejected(self):
        self.assertFalse(valid_trace([TraceRow(1,2)],17))

if __name__ == "__main__": unittest.main()
