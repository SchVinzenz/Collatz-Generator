import unittest
from src.analysis.analyzer import CollatzAnalyzer

class TestCollatzAnalyzer(unittest.TestCase):

    def setUp(self):
        self.analyzer = CollatzAnalyzer()

    def test_cycle_detection(self):
        # Test for cycle detection in known sequences
        self.assertTrue(self.analyzer.detect_cycle(1))  # 1 is a cycle
        self.assertFalse(self.analyzer.detect_cycle(2))  # 2 leads to 1

    def test_binary_analysis(self):
        # Test binary representation analysis
        self.assertEqual(self.analyzer.analyze_binary(5), '101')  # Binary of 5 is '101'
        self.assertEqual(self.analyzer.analyze_binary(10), '1010')  # Binary of 10 is '1010'

    def test_statistics(self):
        # Test statistical analysis of a sequence
        sequence = self.analyzer.generate_sequence(6)  # Collatz sequence starting from 6
        stats = self.analyzer.analyze_statistics(sequence)
        self.assertIn('max', stats)
        self.assertIn('min', stats)
        self.assertIn('average', stats)

if __name__ == '__main__':
    unittest.main()