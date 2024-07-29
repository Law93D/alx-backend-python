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


class TestGithubOrgClient(unittest.TestCase):

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        mock_org.return_value = (
                {"repos_url": "https://api.github.com/orgs/google/repos"})
        # Create an instance of GithubOrgClient
        client = GithubOrgClient("google")
        result = client._public_repos_url
        self.assertEqual(
                (result, "https://api.github.com/orgs/google/repos")
            )

    @patch(
        'client.get_json',
        return_value=[{"name": "repo1"}, {"name": "repo2"}]
    )
    @patch(
        'client.GithubOrgClient._public_repos_url',
        new_callable=PropertyMock
    )
    def test_public_repos(
        self, mock_public_repos_url, mock_get_json
    ):
        # Set up the mocked URL
        mock_public_repos_url.return_value = (
            "https://api.github.com/orgs/google/repos"
        )

        client = GithubOrgClient("google")
        result = client.public_repos()
        self.assertEqual(result, ["repo1", "repo2"])
        mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once_with(
                ("https://api.github.com/orgs/google/repos")
            )

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        client = GithubOrgClient("google")
        result = client.has_license(repo, license_key)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
