import unittest
from src.proofs.prover import Prover

class TestProver(unittest.TestCase):

    def setUp(self):
        self.prover = Prover()

    def test_hypothesis_testing(self):
        result = self.prover.hypothesis_test(1)
        self.assertTrue(result)

    def test_automated_proof_attempt(self):
        proof = self.prover.automated_proof_attempt(5)
        self.assertIsNotNone(proof)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            self.prover.hypothesis_test(-1)

if __name__ == '__main__':
    unittest.main()