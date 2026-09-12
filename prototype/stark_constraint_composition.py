"""Composition simple de contraintes STARK."""
import unittest

def composition(trace, transition_delta, modulus):
    return [(trace[i+1]-trace[i]-transition_delta)%modulus for i in range(len(trace)-1)]

def constraints_hold(trace, delta, modulus):
    return bool(trace) and all(value==0 for value in composition(trace,delta,modulus))

class CompositionTests(unittest.TestCase):
    def test_valid_trace_has_zero_composition(self): self.assertTrue(constraints_hold([2,5,8],3,17))
    def test_invalid_trace_has_nonzero_constraint(self): self.assertFalse(constraints_hold([2,6,8],3,17))
    def test_empty_trace_is_not_a_proof(self): self.assertFalse(constraints_hold([],3,17))

if __name__ == "__main__": unittest.main()
