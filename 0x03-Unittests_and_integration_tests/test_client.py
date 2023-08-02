#!/usr/bin/env python3
"""
Test cases for client.py
"""
import unittest
from unittest.mock import patch, MagicMock
import client
from client import GithubOrgClient
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """
    testcase for the get_json method for returning the json of a client
    """
    @parameterized.expand([
        ("google", {"testing_google": "google"}),
        ("abc", {"testing_abc": "abc"})
    ])
    @patch('client.get_json')
    def test_org(self, org_name, json_result, mock_object):
        """
        test that org returns the correct value
        """
        mock_object.return_value = json_result

        # create instance of GithubOrgClient
        github_org = GithubOrgClient(org_name)
        self.assertEqual(github_org.org, json_result)
        self.assertEqual(github_org.org, json_result)
        url = github_org.ORG_URL.format(org=org_name)
        mock_object.assert_called_once_with(url)
