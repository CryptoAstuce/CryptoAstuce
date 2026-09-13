#!/usr/bin/env python3
"""Toy rollup batch availability checker."""
from hashlib import sha256

def batch_commitment(items: list[bytes]) -> str:
    if not items: raise ValueError("batch must not be empty")
    return sha256(b"batch/v1" + b"".join(sha256(x).digest() for x in items)).hexdigest()

if __name__ == "__main__": print(batch_commitment([b"tx-1", b"tx-2"]))
