"""Triangle Classification & Testing

Author: Irakli Dokhnadze

This module centrally provides a function for classifying triangles as equilateral,
isosceles, or scalene, as well as a right triangle or not, based on given
side lengths.
"""

import unittest
import math

GITHUB_LINK = 'https://github.com/FrillySnake/cs567-triangle-testing'

def classify_triangle(a, b, c):
    """This method accepts three side lengths
    and determine the status of the triangle based on given lengths."""
    try:
        if a == b == c:
            return 'Equilateral'
        if (a == b != c) or (a != b == c) or (a == c != b):
            # we use math.isclose() here because python has limited digits of precision
            # and cannot reliably perform operations on irrational numbers like sqrt(2)
            if math.isclose(a**2 + b**2, c**2):
                return 'Isosceles - Right'
            return 'Isosceles'
        if (a != b != c and a != c):
            if math.isclose(a**2 + b**2, c**2):
                return 'Scalene - Right'
            return 'Scalene'
        return 'NotATriangle'
    except TypeError:
        return 'NotATriangle'

def run_classify_triangle(a, b, c):
    """This method runs the classify_triangle() function with its given inputs
    and prints out the returned output."""
    print(f'classify_triangle({a}, {b}, {c}) = {classify_triangle(a, b, c)}')

# test cases
class TestTriangles(unittest.TestCase):
    """This test class provides a set of two test sets for observing and validating
    the functionality of the triangle classification logic."""
    def test_set_1(self):
        """This set of test cases is aimed at testing unusual or invalid inputs, such as strings."""
        self.assertEqual(classify_triangle('not_a_number', 4, 10),
                         'NotATriangle',
                         'Should not work with non-number inputs')
        self.assertEqual(classify_triangle(True, True, 2**0.5),
                         'Isosceles - Right',
                         'True evaluates to 1; valid triangle')

    def test_set_2(self):
        """This set of test cases is aimed at testing the triangle classification functionality
        to ensure it is correct."""
        self.assertEqual(classify_triangle(3, 4, 5),
                         'Scalene - Right',
                         '3, 4, 5 is a scalene and right triangle')
        self.assertEqual(classify_triangle(1, 1, 2**0.5),
                         'Isosceles - Right',
                         '1, 1, sqrt(2) is an isosceles and right triangle')
        self.assertNotEqual(classify_triangle(5, 5, 5),
                            'NotATriangle',
                            '5, 5, 5 should be an equilateral triangle')
        self.assertEqual(classify_triangle(1, 1, 2.01**0.5),
                         'Isosceles',
                         '1, 1, sqrt(2.01) is an isosceles triangle')
        self.assertNotEqual(classify_triangle(1, 2, 3),
                            'Scalene - Right',
                            '1, 2, 3 should be a non-right scalene triangle')
        self.assertEqual(classify_triangle(124021051234, 124021051234, 124021051234),
                         'Equilateral',
                         '124021051234, 124021051234, 124021051234 is an equilateral triangle')

if __name__ == '__main__':
    run_classify_triangle(1, 2, 3)
    run_classify_triangle(1, 1, 1)
    unittest.main(exit=True)
