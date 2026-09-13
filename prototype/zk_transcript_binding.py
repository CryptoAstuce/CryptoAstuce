#!/usr/bin/env python3
"""Toy ZK transcript binder."""
from hashlib import sha256

def challenge(commitment: bytes, round_number: int, label: str) -> int:
    if round_number < 0: raise ValueError("round must be non-negative")
    data = b"zk-transcript/v1" + round_number.to_bytes(4, "big") + label.encode() + commitment
    return int.from_bytes(sha256(data).digest()[:8], "big")

if __name__ == "__main__": print(challenge(sha256(b"commitment").digest(), 0, "evaluation"))
