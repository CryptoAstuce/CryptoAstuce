import unittest
from commit_classifier import accepted_shas, classify_commit

class ClassifierTests(unittest.TestCase):
    def test_accepts_public_main_commit(self):
        commit={"sha":"base-001","author":"CryptoAstuce","visibility":"public","branch":"main","files":["docs/base.md"],"domain":"Base"}
        self.assertEqual(accepted_shas([commit],"CryptoAstuce"),["base-001"])
    def test_covers_base_hyperliquid_zk_and_fhe(self):
        commits=[{"sha":d.lower()+"-001","author":"CryptoAstuce","visibility":"public","branch":"main","files":["docs/notes.md"],"domain":d} for d in ("Base","Hyperliquid","ZK","FHE")]
        self.assertEqual(len(accepted_shas(commits,"CryptoAstuce")),4)
    def test_reports_rejection_reasons(self):
        d=classify_commit({"sha":"bad-001","author":"other","visibility":"private","branch":"feature","files":[],"is_merge":True},"CryptoAstuce")
        self.assertFalse(d.accepted)
        self.assertGreaterEqual(len(d.reasons),5)

if __name__=="__main__": unittest.main()
