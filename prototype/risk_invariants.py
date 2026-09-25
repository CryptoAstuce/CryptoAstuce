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

def collateral_value(position: Position) -> Decimal:
    """Valeur du collatéral dans l'unité de la dette (quantité × prix)."""
    return position.collateral * position.price

def equity(position: Position) -> Decimal:
    return collateral_value(position) - position.debt

def is_solvent(position: Position) -> bool:
    return collateral_value(position) >= position.debt * position.maintenance_ratio

def bounded_round(value: Decimal, quantum: Decimal) -> Decimal:
    return value.quantize(quantum, rounding=ROUND_DOWN)

class RiskInvariantTests(unittest.TestCase):
    def test_collateral_ratio_protects_solvency(self):
        position = Position(Decimal("150"), Decimal("100"), Decimal("1"), Decimal("1.10"))
        self.assertTrue(is_solvent(position))
    def test_under_collateralized_position_is_rejected(self):
        position = Position(Decimal("105"), Decimal("100"), Decimal("1"), Decimal("1.10"))
        self.assertFalse(is_solvent(position))
    def test_price_drop_breaks_solvency(self):
        # Même quantité de collatéral : la solvabilité dépend du prix.
        healthy = Position(Decimal("150"), Decimal("100"), Decimal("1"), Decimal("1.10"))
        crashed = Position(Decimal("150"), Decimal("100"), Decimal("0.5"), Decimal("1.10"))
        self.assertTrue(is_solvent(healthy))
        self.assertFalse(is_solvent(crashed))
    def test_equity_uses_collateral_value(self):
        position = Position(Decimal("2"), Decimal("100"), Decimal("80"), Decimal("1.10"))
        self.assertEqual(equity(position), Decimal("60"))
    def test_rounding_is_bounded_downward(self):
        self.assertEqual(bounded_round(Decimal("1.239"), Decimal("0.01")), Decimal("1.23"))

if __name__ == "__main__":
    unittest.main()
