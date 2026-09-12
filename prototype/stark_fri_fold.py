"""Réduction FRI déterministe sur un domaine pair."""
import unittest

def fold(values, challenge, modulus):
    if len(values)==0 or len(values)%2: raise ValueError("even domain required")
    half=len(values)//2
    return [(values[i]+challenge*values[i+half])%modulus for i in range(half)]

class FRITests(unittest.TestCase):
    def test_fold_halves_domain(self): self.assertEqual(fold([1,2,3,4],5,17),[16,5])
    def test_odd_domain_rejected(self):
        with self.assertRaises(ValueError): fold([1,2,3],5,17)
    def test_fold_is_deterministic(self): self.assertEqual(fold([1,2],3,17),fold([1,2],3,17))

if __name__ == "__main__": unittest.main()
