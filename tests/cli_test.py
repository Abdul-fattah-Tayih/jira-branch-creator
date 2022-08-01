import os
from sys import argv
from unittest import TestCase
from unittest.mock import patch, Mock
from jira_branch_creator import cli

class MainTest(TestCase):
    @patch.dict(os.environ, {"jira_branch_creator_api_key": "abc"})
    @patch('libraries.git.BranchCreator.create_branch', return_value=None)
    @patch('libraries.issues.JiraIssueResolver.resolve', return_value=Mock())
    @patch('services.branches.BranchService.create_branch', return_value=None)
    @patch('services.branches.BranchService.__init__', return_value=None)
    @patch('jira_branch_creator.input', create=True)
    def test_it_asks_for_variables_the_variables_dont_exist_in_env(
            self,
            input_mock: Mock,
            branch_service_constructor_mock: Mock,
            branch_service_create_branch_mock: Mock,
            issue_resolver_mock: Mock,
            branch_creator_mock: Mock
        ):
        
        input_mock.side_effect = ['abed', '/', 'abed@email.com', 'TEST-123']
        cli()

        branch_service_constructor_mock.assert_called_once_with(**{
            "jira_subdomain": "abed",
            "application_directory": "/",
            "email": "abed@email.com",
            "api_key": "abc", # from the os.environ mock
            "issue_key": argv[1]
        })

        branch_service_create_branch_mock.assert_called_once()
        