GITHUB_LINK = ''

import unittest
import math

# classify_triangle function
def classify_triangle(a, b, c):
    try:
        if (a == b == c):
            return 'Equilateral'
        elif (a == b and a != c != b) or (b == c and b != a != c) or (a == c and a != b != c):
            # we use math.isclose() here because python has limited digits of precision and cannot reliably perform operations on irrational numbers like sqrt(2)
            if math.isclose(a**2 + b**2, c**2):
                return 'Isosceles - Right'
            else:
                return 'Isosceles'
        elif (a != b != c and a != c):
            if math.isclose(a**2 + b**2, c**2):
                return 'Scalene - Right'
            else:
                return 'Scalene'
        else:
            return 'NotATriangle'
    except:
        return 'NotATriangle'

# function 
def run_classify_triangle(a, b, c):
    print(f'classify_triangle({a}, {b}, {c}) = {classify_triangle(a, b, c)}')

class TestTriangles(unittest.TestCase):
    # test unusual or invalid inputs (strings, etc)
    def testSet1(self):
        self.assertEqual(classify_triangle('not_a_number', 4, 10), 'NotATriangle', 'Should not work with non-number inputs')
        self.assertEqual(classify_triangle(True, True, 2**0.5), 'Isosceles - Right', 'True evaluates to 1; valid triangle')

    # test actual functionality (whether it classifies correctly or not)
    def testSet2(self):
        self.assertEqual(classify_triangle(3, 4, 5), 'Scalene - Right', '3, 4, 5 is a scalene and right triangle')
        self.assertEqual(classify_triangle(1, 1, 2**0.5), 'Isosceles - Right', '1, 1, sqrt(2) is an isosceles and right triangle')
        self.assertNotEqual(classify_triangle(5, 5, 5), 'NotATriangle', '5, 5, 5 should be an equilateral triangle')
        self.assertEqual(classify_triangle(1, 1, 2.01**0.5), 'Isosceles', '1, 1, sqrt(2.01) is an isosceles triangle')
        self.assertNotEqual(classify_triangle(1, 2, 3), 'Scalene - Right', '1, 2, 3 should be a non-right scalene triangle')
        self.assertEqual(classify_triangle(124021051234, 124021051234, 124021051234), 'Equilateral', '124021051234, 124021051234, 124021051234 is an equilateral triangle')

if __name__ == '__main__':
    # examples of running the code
    run_classify_triangle(1, 2, 3)
    run_classify_triangle(1, 1, 1)
    
    unittest.main(exit=True) # this runs all of the tests - use this line if running from the command line