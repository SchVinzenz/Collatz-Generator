# test_helpers.py

import unittest
from src.utils.helpers import some_helper_function  # Beispiel für eine Hilfsfunktion

class TestHelpers(unittest.TestCase):

    def test_some_helper_function(self):
        # Beispiel-Test für eine Hilfsfunktion
        self.assertEqual(some_helper_function(2), 4)  # Beispielannahme: Funktion quadriert die Eingabe
        self.assertEqual(some_helper_function(0), 0)
        self.assertEqual(some_helper_function(-3), 9)

if __name__ == '__main__':
    unittest.main()