#!/usr/bin/env python3
"""
Test cases for client.py
"""
import unittest
from unittest.mock import patch, MagicMock, PropertyMock
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

    @parameterized.expand([
        ("google", {"testing_google": "google",
                    "repos_url": "https://google.com"})
    ])
    def test_pulic_repos_url(self, org_name, json_result):
        """
        test the return value for public_repos_url
        """
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_object:
            mock_object.return_value = json_result
            github_org = GithubOrgClient(org_name)
            self.assertEqual(github_org._public_repos_url,
                            json_result['repos_url'])
            mock_object.assert_called_once
