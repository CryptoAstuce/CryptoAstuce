#!/usr/bin/env python3
"""Small EVM revert-data classifier; no RPC or ABI dependency."""

def classify(data: bytes) -> str:
    if data.startswith(bytes.fromhex("08c379a0")): return "Error(string)"
    if data.startswith(bytes.fromhex("4e487b71")): return "Panic(uint256)"
    return "custom-or-unknown"

if __name__ == "__main__": print(classify(bytes.fromhex("08c379a0")))
