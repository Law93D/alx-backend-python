#!/usr/bin/env python3

import unittest
from unittest import TestCase
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos


class TestGithubOrgClient(TestCase):

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json', return_value={'key': 'value'})
    def test_org(self, org_name, mock_get_json):
        client = GithubOrgClient(org_name)
        result = client.org()
        mock_get_json.assert_called_once_with(
                f"https://api.github.com/orgs/{org_name}"
            )
        self.assertEqual(result, {'key': 'value'})


class TestGithubOrgClient(unittest.TestCase):

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        # Set up the mocked payload
        mock_org.return_value = (
                {"repos_url": "https://api.github.com/orgs/google/repos"})
        client = GithubOrgClient("google")
        result = client._public_repos_url
        self.assertEqual(result, "https://api.github.com/orgs/google/repos")


if __name__ == "__main__":
    unittest.main()
