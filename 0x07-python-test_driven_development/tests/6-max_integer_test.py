#!/usr/bin/python3
"""Unittest for the max_integr module"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
        """
        The testCase for the 
        max_integer function.
        """

    def test_regular(self):
        """
        Functions Test with a regular list of ints: 
        that return the max result
        """
        l = [1, 2, 3, 4, 5]
        result = max_integer(l)
        self.assertEqual(result, 5)

    def test_not_int(self):
        """
        Function Test with a list of non-ints and ints:
        should raise a TypeError exception
        """
        l = ["a", "b", 9]
        self.assertRaises(TypeError, max_integer, l)

    def test_empty(self):
        """
        Function test with an empty list: 
        should return None
        """
        l = []
        result = max_integer(l)
        self.assertEqual(result, None)

    def test_negative(self):
        """
        Function Test with a list of negative output: 
        should return the max result
        """
        l = [-2, -6, -1]
        result = max_integer(l)
        self.assertEqual(result, -1)

    def test_float(self):
        """
        Function test with a list of mixed ints, floats:
        should return the max result
        """
        l = [3, 4.5, 2]
        result = max_integer(l)
        self.assertEqual(result, 4.5)

    def test_not_list(self):
        """
        Function Test with a parameter that's not a list: 
        should raise a TypeError
        """
        self.assertRaises(TypeError, max_integer, 7)

    def test_unique(self):
        """
        Function test with a list of one int: 
        should return int value
        """
        l = [45]
        result = max_integer(l)
        self.assertEqual(result, 45)

    def test_identical(self):
        """
        Function Test with a list of identical values: 
        should return the value
        """
        l = [8, 8, 8, 8, 8]
        result = max_integer(l)
        self.assertEqual(result, 8)

    def test_strings(self):
        """
        Test with a list of strings: 
        should return the first string
        """
        l = ["hi", "hello"]
        result = max_integer(l)
        self.assertEqual(result, "hi")

    def test_none(self):
        """
        Function Test with a None as parameter: 
        should raise a TypeError
        """
        self.assertRaises(TypeError, max_integer, None)

if __name__ == '__main__':
    unittest.main()
