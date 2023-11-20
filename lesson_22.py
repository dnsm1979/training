# Tests
import unittest
from fractions import Fraction

# class FractionCalculator:
#     def __init__(self, numerator, denominator):
#         self.fraction = Fraction(numerator, denominator)
#
#     def add(self, other):
#         return self.fraction + other.fraction
#
#     def sub(self, other):
#         return self.fraction - other.fraction
#
#     def mult(self, other):
#         return self.fraction * other.fraction
#
#     def div(self, other):
#         return self.fraction / other.fraction
#
#
#
# class TestFractionCalculator(unittest.TestCase):
#     def test_add(self):
#         frac1 = FractionCalculator(1, 2)
#         frac2 = FractionCalculator(1, 4)
#         self.assertEqual(frac1.add(frac2), Fraction(3, 4))
#
#     def test_sub(self):
#         frac1 = FractionCalculator(1, 5)
#         frac2 = FractionCalculator(1, 2)
#         self.assertEqual(frac1.sub(frac2), Fraction(-3, 10))
#
#     def test_mult(self):
#         frac1 = FractionCalculator(1, 2)
#         frac2 = FractionCalculator(1, 3)
#         self.assertEqual(frac1.mult(frac2), Fraction(1, 6))
#
#     def test_div(self):
#         frac1 = FractionCalculator(1, 2)
#         frac2 = FractionCalculator(1, 3)
#         self.assertEqual(frac1.div(frac2), Fraction(3, 2))
#
#
#
# if __name__ == '__main':
#     unittest.main()

class Calculator:
    def __init__(self, number):
        self.fraction = Fraction(number)

    def add(self, other):
        return self.fraction + other.fraction

    def sub(self, other):
        return self.fraction - other.fraction

    def mult(self, other):
        return self.fraction * other.fraction

    def div(self, other):
        return self.fraction / other.fraction

    def max(self, other):
        return max(self.fraction, other.fraction)

    def min(self, other):
        return min(self.fraction, other.fraction)

    def percent(self, other):
        return self.fraction * other.fraction / 100

class TestCalculator(unittest.TestCase):
    def test_add(self):
        num1 = Calculator(4)
        num2 = Calculator(6)
        self.assertEqual(num1.add(num2), Fraction(10))

    def test_sub(self):
        num1 = Calculator(9)
        num2 = Calculator(5)
        self.assertEqual(num1.sub(num2), Fraction(4))

    def test_mult(self):
        num1 = Calculator(3)
        num2 = Calculator(3)
        self.assertEqual(num1.mult(num2), Fraction(9))

    def test_div(self):
        num1 = Calculator(8)
        num2 = Calculator(2)
        self.assertEqual(num1.div(num2), Fraction(4))

    def test_max(self):
        num1 = Calculator(6)
        num2 = Calculator(3)
        self.assertEqual(num1.max(num2), Fraction(6))

    def test_min(self):
        num1 = Calculator(3)
        num2 = Calculator(8)
        self.assertEqual(num1.min(num2), Fraction(3))

    def test_percent(self):
        num1 = Calculator(4)
        num2 = Calculator(8)
        self.assertEqual(num1.percent(num2), Fraction(0.5))




if __name__ == '__main':
    unittest.main()