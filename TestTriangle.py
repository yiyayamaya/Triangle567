# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

#from TriangleOriginal import classifyTriangle
from TriangleImproved import classifyTriangle


# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testInvalidInput1(self):
        self.assertEqual(classifyTriangle("3", "", ""), "InvalidInput")

    def testInvalidInput2(self):
        self.assertEqual(classifyTriangle(-1, -1, -1), "InvalidInput")

    def testInvalidInput3(self):
        self.assertEqual(classifyTriangle(999, 999, 999), "InvalidInput")

    def testRightTriangle1(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right')

    def testRightTriangle2(self):
        self.assertEqual(classifyTriangle(50, 30, 40), 'Right')

    def testRightTriangle3(self):
        self.assertEqual(classifyTriangle(3, 5, 4), 'Right')

    def testNotTriangle1(self):
        self.assertEqual(classifyTriangle(1, 1, 2), 'NotATriangle')

    def testNotTriangle2(self):
        self.assertEqual(classifyTriangle(1, 1, 3), 'NotATriangle')

    def testIsoceles1(self):
        self.assertEqual(classifyTriangle(2, 2, 3), 'Isoceles')

    def testIsoceles2(self):
        self.assertEqual(classifyTriangle(3, 2, 2), 'Isoceles')

    def testIsoceles3(self):
        self.assertEqual(classifyTriangle(2, 3, 2), 'Isoceles')


    def testEquilateral1(self):
        self.assertEqual(classifyTriangle(2, 2, 2), 'Equilateral')

    def testScalene1(self):
        self.assertEqual(classifyTriangle(2, 3, 4), 'Scalene')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
