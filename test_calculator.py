#https://github.com/hiteshk2k6/lab11--HK---DC-.git
#Hitesh K
#Nobody


import unittest
import calculator


class TestCalculator(unittest.TestCase):

    def test_multiply(self):
        # Test basic multiplication (using mul function)
        self.assertEqual(calculator.mul(3, 4), 12)
        self.assertEqual(calculator.mul(-2, 5), -10)
        self.assertEqual(calculator.mul(0, 10), 0)
        self.assertAlmostEqual(calculator.mul(2.5, 4), 10.0)

    def test_divide(self):
        # Test basic division (using div function - remember: div(a, b) returns b / a)
        self.assertEqual(calculator.div(2, 10), 5)
        self.assertEqual(calculator.div(5, 20), 4)
        self.assertAlmostEqual(calculator.div(3, 9), 3.0)

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

    def test_hypotenuse(self):
        # Test Pythagorean theorem: hypotenuse of 3-4-5 triangle
        self.assertAlmostEqual(calculator.hypotenuse(3, 4), 5.0)

        # Test with other values
        self.assertAlmostEqual(calculator.hypotenuse(5, 12), 13.0)
        self.assertAlmostEqual(calculator.hypotenuse(1, 1), 1.414213562, places=5)

        # Test with negative values (should raise ValueError)
        with self.assertRaises(ValueError):
            calculator.hypotenuse(-3, 4)
        with self.assertRaises(ValueError):
            calculator.hypotenuse(3, -4)

    def test_sqrt(self):
        # Test basic square roots
        self.assertAlmostEqual(calculator.square_root(4), 2.0)
        self.assertAlmostEqual(calculator.square_root(9), 3.0)
        self.assertAlmostEqual(calculator.square_root(16), 4.0)
        self.assertAlmostEqual(calculator.square_root(2), 1.414213562, places=5)
        self.assertAlmostEqual(calculator.square_root(0), 0.0)

        # Test negative value (should raise ValueError)
        with self.assertRaises(ValueError):
            calculator.square_root(-4)


# Do not touch this
if __name__ == "__main__":
    unittest.main()