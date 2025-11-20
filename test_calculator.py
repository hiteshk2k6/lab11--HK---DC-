#https://github.com/hiteshk2k6/lab11--HK---DC-.git
#Hitesh K
#Nobody

import unittest
import calculator


class TestCalculator(unittest.TestCase):

    def test_add(self):
        # Test addition
        self.assertEqual(calculator.add(3, 5), 8)
        self.assertEqual(calculator.add(-2, 7), 5)
        self.assertAlmostEqual(calculator.add(2.5, 3.7), 6.2)

    def test_subtract(self):
        # Test subtraction
        self.assertEqual(calculator.subtract(10, 4), 6)
        self.assertEqual(calculator.subtract(-5, 3), -8)
        self.assertAlmostEqual(calculator.subtract(7.5, 2.3), 5.2)

    def test_exponent(self):
        # Test exponentiation (using exp function)
        self.assertEqual(calculator.exp(2, 3), 8)
        self.assertEqual(calculator.exp(5, 2), 25)
        self.assertAlmostEqual(calculator.exp(2, 0.5), 1.414213562, places=5)

    def test_multiply(self):
        # Test basic multiplication (using mul function)
        self.assertEqual(calculator.mul(3, 4), 12)
        self.assertEqual(calculator.mul(-2, 5), -10)
        self.assertEqual(calculator.mul(0, 10), 0)
        self.assertAlmostEqual(calculator.mul(2.5, 4), 10.0)
        self.assertEqual(calculator.mul(-3, -7), 21)
        self.assertAlmostEqual(calculator.mul(0.5, 0.2), 0.1)
        self.assertEqual(calculator.mul(7, 8), 56)
        self.assertAlmostEqual(calculator.mul(1.5, 3), 4.5)
        self.assertEqual(calculator.mul(100, 0), 0)

    def test_divide(self):
        # Test basic division (using div function - remember: div(a, b) returns b / a)
        self.assertEqual(calculator.div(2, 10), 5)
        self.assertEqual(calculator.div(5, 20), 4)
        self.assertAlmostEqual(calculator.div(3, 9), 3.0)
        self.assertAlmostEqual(calculator.div(4, 1), 0.25)
        self.assertEqual(calculator.div(10, 100), 10)
        self.assertAlmostEqual(calculator.div(8, 4), 0.5)
        self.assertEqual(calculator.div(7, 49), 7)
        self.assertAlmostEqual(calculator.div(2.5, 10), 4.0)

        # Test division by zero raises error
        with self.assertRaises(ZeroDivisionError):
            calculator.div(0, 10)

    def test_log_invalid_argument(self):
        # Test that logarithm raises ValueError for invalid inputs

        # Negative base
        with self.assertRaises(ValueError):
            calculator.logarithm(-2, 8)

        # Negative argument
        with self.assertRaises(ValueError):
            calculator.logarithm(2, -8)

        # Zero base
        with self.assertRaises(ValueError):
            calculator.logarithm(0, 8)

        # Zero argument
        with self.assertRaises(ValueError):
            calculator.logarithm(2, 0)

        # Base of 1 (undefined)
        with self.assertRaises(ValueError):
            calculator.logarithm(1, 8)

        # Both negative
        with self.assertRaises(ValueError):
            calculator.logarithm(-5, -10)

        # Negative base with positive argument
        with self.assertRaises(ValueError):
            calculator.logarithm(-3, 9)

        # Zero argument with positive base
        with self.assertRaises(ValueError):
            calculator.logarithm(10, 0)

    def test_hypotenuse(self):
        # Test Pythagorean theorem: hypotenuse of 3-4-5 triangle
        self.assertAlmostEqual(calculator.hypotenuse(3, 4), 5.0)

        # Test with other values
        self.assertAlmostEqual(calculator.hypotenuse(5, 12), 13.0)
        self.assertAlmostEqual(calculator.hypotenuse(1, 1), 1.414213562, places=5)
        self.assertAlmostEqual(calculator.hypotenuse(6, 8), 10.0)
        self.assertAlmostEqual(calculator.hypotenuse(0, 5), 5.0)
        self.assertAlmostEqual(calculator.hypotenuse(8, 15), 17.0)
        self.assertAlmostEqual(calculator.hypotenuse(2, 2), 2.828427125, places=5)
        self.assertAlmostEqual(calculator.hypotenuse(7, 24), 25.0)

        # Test with negative values (should raise ValueError)
        with self.assertRaises(ValueError):
            calculator.hypotenuse(-3, 4)
        with self.assertRaises(ValueError):
            calculator.hypotenuse(3, -4)
        with self.assertRaises(ValueError):
            calculator.hypotenuse(-5, -12)

    def test_sqrt(self):
        # Test basic square roots
        self.assertAlmostEqual(calculator.square_root(4), 2.0)
        self.assertAlmostEqual(calculator.square_root(9), 3.0)
        self.assertAlmostEqual(calculator.square_root(16), 4.0)
        self.assertAlmostEqual(calculator.square_root(2), 1.414213562, places=5)
        self.assertAlmostEqual(calculator.square_root(0), 0.0)
        self.assertAlmostEqual(calculator.square_root(25), 5.0)
        self.assertAlmostEqual(calculator.square_root(100), 10.0)


# Do not touch this
if __name__ == "__main__":
    unittest.main()