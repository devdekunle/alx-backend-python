#!/usr/bin/env python3
"""
Module that contains tests for util.access_nested_map
"""
from utils import access_nested_map, get_json, memoize
import unittest
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from typing import (
    Any,
    Mapping,
    Sequence,
    Dict,
    Callable
)

class TestAccessNestedMap(unittest.TestCase):
    """
    tests class for the access_nested_map
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping,
                          path: Sequence, expected: Any) -> None:
        """ tests for access_nested_map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "KeyError: 'a'"),
        ({"a": 1}, ("a", "b"), "KeyError: 'b'")
    ])
    def test_access_nested_map_exception(self,
        nested_map: Mapping, path: Sequence,
        expected: Any) -> None:
        with self.assertRaises(KeyError, msg=expected):
            access_nested_map(nested_map, path)

class TestGetJson(unittest.TestCase):
    """
    Test for get_json method
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('utils.requests')
    def test_get_json(self, test_url, test_payload, mocked_requests):
        """
        mock test for the get_json method
        """
        mock_response = MagicMock()
        mock_response.json.return_value = test_payload

        mocked_requests.get.return_value = mock_response
        self.assertEqual(get_json(test_url), test_payload)
        mocked_requests.get.assert_called_once_with(test_url)

class TestMemoize(unittest.TestCase):
    """
    Test case for memoize function
    """
    def test_memoize(self):
        """
        test memoize
        """
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        test_instance = TestClass()
        with patch.object(TestClass, 'a_method') as mock_object:
            mock_object.return_value = 42
            result1 = test_instance.a_property
            result2 = test_instance.a_property
            mock_object.assert_called_once()

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
