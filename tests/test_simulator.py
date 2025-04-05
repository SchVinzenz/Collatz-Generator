import unittest
from src.simulation.simulator import CollatzSequence

class TestCollatzSequence(unittest.TestCase):

    def setUp(self):
        self.sequence = CollatzSequence()

    def test_collatz_sequence(self):
        self.assertEqual(self.sequence.generate(1), [1])
        self.assertEqual(self.sequence.generate(2), [2, 1])
        self.assertEqual(self.sequence.generate(3), [3, 10, 5, 16, 8, 4, 2, 1])
        self.assertEqual(self.sequence.generate(4), [4, 2, 1])
        self.assertEqual(self.sequence.generate(5), [5, 16, 8, 4, 2, 1])

    def test_collatz_sequence_with_large_number(self):
        result = self.sequence.generate(27)
        self.assertEqual(result[-1], 1)  # Ensure the sequence ends with 1

    def test_invalid_start_value(self):
        with self.assertRaises(ValueError):
            self.sequence.generate(0)  # Collatz sequence is not defined for 0
        with self.assertRaises(ValueError):
            self.sequence.generate(-5)  # Collatz sequence is not defined for negative numbers

if __name__ == '__main__':
    unittest.main()