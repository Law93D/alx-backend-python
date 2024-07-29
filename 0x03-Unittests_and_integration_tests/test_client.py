#!/usr/bin/env python3
from unittest import TestCase
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos


class TestGithubOrgClient(unittest.TestCase):

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value."""
        client = GithubOrgClient(org_name)
        client.org()
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """Test that GithubOrgClient returns the expected value."""
        mock_org.return_value = {"repos_url": "http://some_url.com/repos"}
        client = GithubOrgClient("org_name")
        self.assertEqual(client._public_repos_url,
                         mock_org.return_value["repos_url"])

    @patch('client.get_json')
    @patch(
            'client.GithubOrgClient._public_repos_url',
            new_callable=PropertyMock
        )
    def test_public_repos(self, mock_public_repos_url, mock_get_json):

        mock_public_repos_url.return_value = "http://some_url.com/repos"
        mock_get_json.return_value = [{"name": "repo1"}, {"name": "repo2"}]
        client = GithubOrgClient("org_name")
        with patch.object(client, '_public_repos_url', mock_public_repos_url):
            self.assertEqual(client.public_repos(), ["repo1", "repo2"])
            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with("http://some_url.com/repos")

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test that GithubOrgClient.has_license returns the correct result."""
        client = GithubOrgClient("org_name")
        self.assertEqual(client.has_license(repo, license_key), expected)


@parameterized_class([
    {
        "org_payload": org_payload,
        "repos_payload": repos_payload,
        "expected_repos": expected_repos,
        "apache2_repos": apache2_repos,
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test for GithubOrgClient.public_repos"""

    @classmethod
    def setUpClass(cls):
        """Set up class for integration tests"""
        cls.get_patcher = patch('requests.get', side_effect=cls.get_patched)
        cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """Tear down class for integration tests"""
        cls.get_patcher.stop()

    @staticmethod
    def get_patched(url):
        """Patch method to return the appropriate fixture"""
        if "orgs" in url:
            return MockResponse(TestIntegrationGithubOrgClient.org_payload)
        if "repos" in url:
            return MockResponse(TestIntegrationGithubOrgClient.repos_payload)

    def test_public_repos(self):
        """Test GithubOrgClient.public_repos"""
        client = GithubOrgClient("org_name")
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """Test GithubOrgClient.public_repos with license"""
        client = GithubOrgClient("org_name")
        self.assertEqual(client.public_repos(license="apache-2.0"),
                         self.apache2_repos)


class MockResponse:
    """Mock response for requests.get"""
    def __init__(self, json_data):
        self.json_data = json_data

    def json(self):
        return self.json_data


if __name__ == "__main__":
    unittest.main()
