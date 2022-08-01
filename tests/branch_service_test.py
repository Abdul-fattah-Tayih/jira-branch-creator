from email.mime import application
from unittest import TestCase
from unittest.mock import Mock, patch
from libraries.issues import JiraIssueResolver
from services.branches import BranchService

class BranchServiceTest(TestCase):
    @patch('libraries.issues.JiraIssueResolver.resolve')
    def test_it_retrieves_jira_issue(self, jira_issue_resolver_mock: Mock):
        jira_issue_mock = Mock()
        jira_issue_mock.type = 'Story'
        jira_issue_mock.key = 'TEST-123'
        jira_issue_mock.title = 'Test story'
        jira_issue_resolver_mock.return_value = jira_issue_mock

        branch_service = BranchService('abed@email.com', '123', 'TEST-123', 'abed', '~')
        branch_service.create_branch()

        jira_issue_resolver_mock.assert_called_once()

    @patch('libraries.git.BranchCreator.create_branch')
    @patch('libraries.issues.JiraIssueResolver.resolve')
    def test_it_creates_branch_after_retrieving_issues(self, resolve_mock: Mock, create_branch_mock: Mock):
        jira_issue_mock = Mock()
        jira_issue_mock.type = 'Story'
        jira_issue_mock.key = 'TEST-123'
        jira_issue_mock.title = 'Test story'
        resolve_mock.return_value = jira_issue_mock

        branch_service = BranchService('abed@email.com', '123', 'TEST-123', 'abed', '~')
        branch_service.create_branch()

        resolve_mock.assert_called_once()
        create_branch_mock.assert_called_once()