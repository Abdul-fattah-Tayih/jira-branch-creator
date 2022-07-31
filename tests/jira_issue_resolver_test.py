import unittest
from unittest.mock import Mock, patch
from requests.auth import HTTPBasicAuth
from libraries.issues import JiraIssue, JiraIssueResolver

class JiraIssueResolverTest(unittest.TestCase):
    @patch('requests.request')
    def test_issue_resolver_calls_jira_rest_api_correctly(self, request_mock: Mock):
        response_mock = Mock(status_code=200)
        response_mock.text = """{
            "key": "test-123",
            "fields": {
                "summary": "I am a test issue",
                "issuetype": {
                    "name": "Story"
                }
            }
        }"""

        request_mock.return_value = response_mock
        JiraIssueResolver('abc', 'test-123', 'a@b.com', '123').retrieve()

        request_mock.assert_called_once_with(
            'GET',
            'https://abc.atlassian.net/rest/api/3/issue/test-123?fields=summary,issuetype',
            headers={"Accept": "application/json"},
            auth=HTTPBasicAuth('a@b.com', '123')
        )

    @patch('requests.request')
    def test_it_returns_a_valid_jira_issue_object(self, request_mock: Mock):
        response_mock = Mock()
        response_mock.status_code = 200
        response_mock.text = """{
            "key": "test-123",
            "fields": {
                "summary": "I am a test issue",
                "issuetype": {
                    "name": "Story"
                }
            }
        }"""

        request_mock.return_value = response_mock

        resolver = JiraIssueResolver('abc', 'test-123', 'a@b.com', '123')
        issue = resolver.retrieve()

        self.assertEquals(issue.__class__, JiraIssue)
        self.assertEquals(issue.title, 'I am a test issue')
        self.assertEquals(issue.type, 'Story')
        self.assertEquals(issue.key, 'test-123')

    @patch('requests.request')
    def test_it_exits_if_jira_api_response_is_not_200(self, request_mock: Mock):
        response_mock = Mock()
        response_mock.status_code = 401
        request_mock.return_value = response_mock

        self.assertRaises(SystemExit, lambda: JiraIssueResolver('abc', 'test-123', 'a@b.com', '123').retrieve())
