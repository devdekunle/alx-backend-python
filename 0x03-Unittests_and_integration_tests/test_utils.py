#!/usr/bin/env python3
"""
Module that contains tests for util.access_nested_map
"""
from utils import access_nested_map
import unittest
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


