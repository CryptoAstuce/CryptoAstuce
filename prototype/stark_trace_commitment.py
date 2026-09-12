"""Engagement déterministe d'une trace STARK par hachage."""
import hashlib
import unittest

def commit_trace(values, salt: str = "") -> str:
    payload = salt + ":" + ",".join(str(value) for value in values)
    return hashlib.sha256(payload.encode()).hexdigest()

def opens(commitment: str, values, salt: str = "") -> bool:
    return commitment == commit_trace(values, salt)

class CommitmentTests(unittest.TestCase):
    def test_same_trace_has_same_commitment(self):
        self.assertEqual(commit_trace([2,5,8], "s"), commit_trace([2,5,8], "s"))
    def test_modified_trace_does_not_open(self):
        commitment = commit_trace([2,5,8], "s")
        self.assertFalse(opens(commitment, [2,6,8], "s"))
    def test_salt_separates_domains(self):
        self.assertNotEqual(commit_trace([1], "a"), commit_trace([1], "b"))

if __name__ == "__main__": unittest.main()
