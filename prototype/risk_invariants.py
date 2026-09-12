"""Invariants pédagogiques de risque pour Hyperliquid / HyperEVM."""
from dataclasses import dataclass
from decimal import Decimal, ROUND_DOWN
import unittest

@dataclass(frozen=True)
class Position:
    collateral: Decimal
    debt: Decimal
    price: Decimal
    maintenance_ratio: Decimal

def equity(position: Position) -> Decimal:
    return position.collateral + position.price - position.debt

def is_solvent(position: Position) -> bool:
    return position.collateral >= position.debt * position.maintenance_ratio

def bounded_round(value: Decimal, quantum: Decimal) -> Decimal:
    return value.quantize(quantum, rounding=ROUND_DOWN)

class RiskInvariantTests(unittest.TestCase):
    def test_collateral_ratio_protects_solvency(self):
        position = Position(Decimal("150"), Decimal("100"), Decimal("1"), Decimal("1.10"))
        self.assertTrue(is_solvent(position))
    def test_under_collateralized_position_is_rejected(self):
        position = Position(Decimal("105"), Decimal("100"), Decimal("1"), Decimal("1.10"))
        self.assertFalse(is_solvent(position))
    def test_rounding_is_bounded_downward(self):
        self.assertEqual(bounded_round(Decimal("1.239"), Decimal("0.01")), Decimal("1.23"))

if __name__ == "__main__":
    unittest.main()
