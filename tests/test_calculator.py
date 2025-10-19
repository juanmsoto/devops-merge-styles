import unittest

from calculator import Calculator


class CalculatorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_addition(self) -> None:
        self.assertEqual(self.calculator.add(3, 5), 8)

    def test_subtraction(self) -> None:
        self.assertEqual(self.calculator.subtract(10, 4), 6)

    def test_multiplication(self) -> None:
        self.assertEqual(self.calculator.multiply(7, 6), 42)

    def test_division(self) -> None:
        self.assertAlmostEqual(self.calculator.divide(10, 4), 2.5)

    def test_division_by_zero_raises_value_error(self) -> None:
        with self.assertRaises(ValueError):
            self.calculator.divide(5, 0)


if __name__ == "__main__":
    unittest.main()
