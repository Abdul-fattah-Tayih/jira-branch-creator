import os
from unittest import TestCase
from click.testing import CliRunner
from unittest.mock import patch, Mock

class CliTest(TestCase):
    @patch('libraries.git.BranchCreator.create_branch', return_value=None)
    @patch('libraries.issues.JiraIssueResolver.resolve', return_value=Mock())
    @patch('services.branches.BranchService.create_branch', return_value=None)
    @patch('services.branches.BranchService.__init__', return_value=None)
    def test_it_requires_issue_key(
            self,
            branch_service_constructor_mock: Mock,
            branch_service_create_branch_mock: Mock,
            issue_resolver_mock: Mock,
            branch_creator_mock: Mock
        ):
        
        env = os.environ
        env['jira_branch_creator_email'] = 'my@email'
        env['jira_branch_creator_api_key'] = 'api_key_123'
        env['jira_branch_creator_jira_subdomain'] = 'my_subdomain'

        with patch.dict('jira_branch_creator.os.environ', env):
            from jira_branch_creator import cli
            runner = CliRunner()
            result = runner.invoke(cli)

            assert result.exit_code == 2
            assert "Missing argument 'ISSUE_KEY'" in result.output

            branch_service_constructor_mock.assert_not_called()
            branch_service_create_branch_mock.assert_not_called()

    @patch('libraries.git.BranchCreator.create_branch', return_value=None)
    @patch('libraries.issues.JiraIssueResolver.resolve', return_value=Mock())
    @patch('services.branches.BranchService.create_branch', return_value=None)
    @patch('services.branches.BranchService.__init__', return_value=None)
    def test_it_fails_and_asks_for_jira_username_if_it_doesnt_exist_in_env(
            self,
            branch_service_constructor_mock: Mock,
            branch_service_create_branch_mock: Mock,
            issue_resolver_mock: Mock,
            branch_creator_mock: Mock
        ):
        # TODO fix
        self.skipTest('Works in isolation, but fails with suite')
        
        env = os.environ
        env.pop('jira_branch_creator_email', None)
        env.pop('jira_branch_creator_api_key', None)
        env.pop('jira_branch_creator_jira_subdomain', None)

        with patch.dict('jira_branch_creator.os.environ', env, True):
            from jira_branch_creator import cli
            runner = CliRunner()
            result = runner.invoke(cli, ['TEST-123'])

            assert result.exit_code == 2
            assert "Missing argument 'JIRA_USERNAME'" in result.output

            branch_service_constructor_mock.assert_not_called()
            branch_service_create_branch_mock.assert_not_called()

    @patch('libraries.git.BranchCreator.create_branch', return_value=None)
    @patch('libraries.issues.JiraIssueResolver.resolve', return_value=Mock())
    @patch('services.branches.BranchService.create_branch', return_value=None)
    @patch('services.branches.BranchService.__init__', return_value=None)
    def test_it_fails_and_asks_for_jira_api_key_if_it_doesnt_exist_in_env(
            self,
            branch_service_constructor_mock: Mock,
            branch_service_create_branch_mock: Mock,
            issue_resolver_mock: Mock,
            branch_creator_mock: Mock
        ):
        # TODO fix
        self.skipTest('Works in isolation, but fails with suite')

        env = os.environ
        env.pop('jira_branch_creator_email', None)
        env.pop('jira_branch_creator_api_key', None)
        env.pop('jira_branch_creator_jira_subdomain', None)

        with patch.dict('jira_branch_creator.os.environ', env, True):
            from jira_branch_creator import cli
            runner = CliRunner()
            result = runner.invoke(cli, ['TEST-123', 'my@email.com'])

            assert result.exit_code == 2
            assert "Missing argument 'JIRA_API_KEY'" in result.output

            branch_service_constructor_mock.assert_not_called()
            branch_service_create_branch_mock.assert_not_called()


    @patch('libraries.git.BranchCreator.create_branch', return_value=None)
    @patch('libraries.issues.JiraIssueResolver.resolve', return_value=Mock())
    @patch('services.branches.BranchService.create_branch', return_value=None)
    @patch('services.branches.BranchService.__init__', return_value=None)
    def test_it_fails_and_asks_for_jira_subdomain_if_it_doesnt_exist_in_env(
            self,
            branch_service_constructor_mock: Mock,
            branch_service_create_branch_mock: Mock,
            issue_resolver_mock: Mock,
            branch_creator_mock: Mock
        ):
        # TODO fix
        self.skipTest('Works in isolation, but fails with suite')

        env = os.environ
        env.pop('jira_branch_creator_email', None)
        env.pop('jira_branch_creator_api_key', None)
        env.pop('jira_branch_creator_jira_subdomain', None)

        with patch.dict('jira_branch_creator.os.environ', env, True):
            from jira_branch_creator import cli
            runner = CliRunner()
            result = runner.invoke(cli, ['TEST-123', 'my@email.com', 'api_key_123'])

            assert result.exit_code == 2
            assert "Missing argument 'JIRA_SUBDOMAIN'" in result.output

            branch_service_constructor_mock.assert_not_called()
            branch_service_create_branch_mock.assert_not_called()

    @patch('libraries.git.BranchCreator.create_branch', return_value=None)
    @patch('libraries.issues.JiraIssueResolver.resolve', return_value=Mock())
    @patch('services.branches.BranchService.create_branch', return_value=None)
    @patch('services.branches.BranchService.__init__', return_value=None)
    def test_it_doesnt_require_arguements_if_theyre_set_in_env(
            self,
            branch_service_constructor_mock: Mock,
            branch_service_create_branch_mock: Mock,
            issue_resolver_mock: Mock,
            branch_creator_mock: Mock
        ):
        
        env = os.environ
        env['jira_branch_creator_email'] = 'my@email'
        env['jira_branch_creator_api_key'] = 'api_key_123'
        env['jira_branch_creator_jira_subdomain'] = 'my_subdomain'

        with patch.dict('jira_branch_creator.os.environ', env):
            from jira_branch_creator import cli
            runner = CliRunner()
            result = runner.invoke(cli, ['TEST-123'])

            assert result.exit_code == 0
            branch_service_constructor_mock.assert_called_once_with(
                env['jira_branch_creator_email'],
                env['jira_branch_creator_api_key'],
                'TEST-123',
                env['jira_branch_creator_jira_subdomain'],
                '.',
                None,
                None
            )

            branch_service_create_branch_mock.assert_called_once()

    @patch('libraries.git.BranchCreator.create_branch', return_value=None)
    @patch('libraries.issues.JiraIssueResolver.resolve', return_value=Mock())
    @patch('services.branches.BranchService.create_branch', return_value=None)
    @patch('services.branches.BranchService.__init__', return_value=None)
    def test_it_accepts_target_directory_option(
            self,
            branch_service_constructor_mock: Mock,
            branch_service_create_branch_mock: Mock,
            issue_resolver_mock: Mock,
            branch_creator_mock: Mock
        ):
        
        env = os.environ
        env['jira_branch_creator_email'] = 'my@email'
        env['jira_branch_creator_api_key'] = 'api_key_123'
        env['jira_branch_creator_jira_subdomain'] = 'my_subdomain'

        with patch.dict('jira_branch_creator.os.environ', env):
            from jira_branch_creator import cli
            runner = CliRunner()
            result = runner.invoke(cli, ['TEST-123', '--target-dir', '/'])

            assert result.exit_code == 0
            branch_service_constructor_mock.assert_called_once_with(
                env['jira_branch_creator_email'],
                env['jira_branch_creator_api_key'],
                'TEST-123',
                env['jira_branch_creator_jira_subdomain'],
                '/',
                None,
                None
            )

            branch_service_create_branch_mock.assert_called_once()

    @patch('libraries.git.BranchCreator.create_branch', return_value=None)
    @patch('libraries.issues.JiraIssueResolver.resolve', return_value=Mock())
    @patch('services.branches.BranchService.create_branch', return_value=None)
    @patch('services.branches.BranchService.__init__', return_value=None)
    def test_it_accepts_branch_word_limit_option(
            self,
            branch_service_constructor_mock: Mock,
            branch_service_create_branch_mock: Mock,
            issue_resolver_mock: Mock,
            branch_creator_mock: Mock
        ):
        
        env = os.environ
        env['jira_branch_creator_email'] = 'my@email'
        env['jira_branch_creator_api_key'] = 'api_key_123'
        env['jira_branch_creator_jira_subdomain'] = 'my_subdomain'

        with patch.dict('jira_branch_creator.os.environ', env):
            from jira_branch_creator import cli
            runner = CliRunner()
            result = runner.invoke(cli, ['TEST-123', '--branch-word-limit', 5])

            assert result.exit_code == 0
            branch_service_constructor_mock.assert_called_once_with(
                env['jira_branch_creator_email'],
                env['jira_branch_creator_api_key'],
                'TEST-123',
                env['jira_branch_creator_jira_subdomain'],
                '.',
                '5',
                None
            )

            branch_service_create_branch_mock.assert_called_once()
    
    @patch('libraries.git.BranchCreator.create_branch', return_value=None)
    @patch('libraries.issues.JiraIssueResolver.resolve', return_value=Mock())
    @patch('services.branches.BranchService.create_branch', return_value=None)
    @patch('services.branches.BranchService.__init__', return_value=None)
    def test_it_accepts_branch_type_option(
            self,
            branch_service_constructor_mock: Mock,
            branch_service_create_branch_mock: Mock,
            issue_resolver_mock: Mock,
            branch_creator_mock: Mock
        ):
        
        env = os.environ
        env['jira_branch_creator_email'] = 'my@email'
        env['jira_branch_creator_api_key'] = 'api_key_123'
        env['jira_branch_creator_jira_subdomain'] = 'my_subdomain'

        with patch.dict('jira_branch_creator.os.environ', env):
            from jira_branch_creator import cli
            runner = CliRunner()
            result = runner.invoke(cli, ['TEST-123', '--branch-type', 'hotfix'])

            assert result.exit_code == 0
            branch_service_constructor_mock.assert_called_once_with(
                env['jira_branch_creator_email'],
                env['jira_branch_creator_api_key'],
                'TEST-123',
                env['jira_branch_creator_jira_subdomain'],
                '.',
                None,
                'hotfix'
            )

            branch_service_create_branch_mock.assert_called_once()
        