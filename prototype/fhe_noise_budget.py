#!/usr/bin/env python3
"""Toy FHE noise-budget tracker for BFV/BGV/CKKS discussions.

It models budget consumption only; it is not a ciphertext implementation.
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class NoiseBudget:
    remaining: int

    def consume(self, multiplication_cost: int = 0, addition_cost: int = 1) -> "NoiseBudget":
        cost = multiplication_cost + addition_cost
        if cost < 0 or cost > self.remaining:
            raise ValueError("invalid or exhausted noise budget")
        return NoiseBudget(self.remaining - cost)


def demo() -> None:
    budget = NoiseBudget(12)
    after_add = budget.consume(addition_cost=1)
    after_mul = after_add.consume(multiplication_cost=4, addition_cost=1)
    print(budget.remaining, after_add.remaining, after_mul.remaining)
    print("the budget is a planning signal, not a security proof")


if __name__ == "__main__":
    demo()
