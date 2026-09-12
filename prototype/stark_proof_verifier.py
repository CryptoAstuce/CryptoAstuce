"""Vérification finale d'un paquet de preuve STARK."""
import hashlib
import unittest

def proof_digest(trace, commitment, claimed_result):
    data=":".join([commitment, str(claimed_result), ",".join(map(str,trace))])
    return hashlib.sha256(data.encode()).hexdigest()

def verify_proof(trace, commitment, claimed_result, digest):
    return bool(trace) and digest == proof_digest(trace,commitment,claimed_result)

class ProofTests(unittest.TestCase):
    def test_valid_package_verifies(self):
        t=[2,5,8]; c="root"; d=proof_digest(t,c,8)
        self.assertTrue(verify_proof(t,c,8,d))
    def test_changed_claim_fails(self):
        t=[2,5,8]; d=proof_digest(t,"root",8)
        self.assertFalse(verify_proof(t,"root",9,d))
    def test_empty_trace_fails(self): self.assertFalse(verify_proof([],"root",0,"x"))

if __name__ == "__main__": unittest.main()
