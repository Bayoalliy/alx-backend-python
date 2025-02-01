#!/usr/bin/env python3
"""
In this task you will write the first unit test for
utils.access_nested_map.

Create a TestAccessNestedMap class that inherits
from unittest.TestCase.

Implement the TestAccessNestedMap.test_access_nested_map
method to test that the method returns what it is supposed to.

Decorate the method with @parameterized.expand to test
the function for following inputs:

nested_map={"a": 1}, path=("a",)
nested_map={"a": {"b": 2}}, path=("a",)
nested_map={"a": {"b": 2}}, path=("a", "b")
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """Tests access_nested_map function"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b",), 2)
        ])
    def test_access_nested_map(self, a, b, expected):
        """check if result is espected"""
        self.assertEqual(access_nested_map(a, b), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
        ])
    def test_access_nested_map_exception(self, a, b, expected):
        """checks if exception is raised correctly"""
        self.assertRaises(expected, access_nested_map, a, b)


class TestGetJson(unittest.TestCase):
    """tests get_json functio"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
        ])
    def test_get_json(self, url, expected):
        """replaces the value of response variable"""
        with patch('requests.get') as mock_get:
            mock = Mock()
            mock.json.return_value = expected
            mock_get.return_value = mock
            self.assertEqual(get_json(url), expected)
            mock_get.assert_called_once_with(url)


class TestMemoize(unittest.TestCase):
    """tests the memoize function"""
    def test_memoize(self):
        """defines class with methods to be memoized"""
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        testClass = TestClass()
        with patch.object(testClass, 'a_method') as mock_method:
            mock_method.return_value = 42

            self.assertEqual(testClass.a_property, 42)
            self.assertEqual(testClass.a_property, 42)
            mock_method.assert_called_once()
