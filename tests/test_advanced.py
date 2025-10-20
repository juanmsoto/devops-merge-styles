import unittest
from calculator.advanced import power

class TestAdvanced(unittest.TestCase):
    def test_power_positive(self):
        self.assertEqual(power(2, 3), 8)

    def test_power_zero(self):
        self.assertEqual(power(5, 0), 1)

    def test_power_fraction(self):
        self.assertAlmostEqual(power(9, 0.5), 3.0)

if __name__ == "__main__":
    unittest.main()
