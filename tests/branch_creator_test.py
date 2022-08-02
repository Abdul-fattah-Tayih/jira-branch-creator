import unittest
from unittest.mock import Mock, patch
from libraries.git import BranchCreator

from libraries.issues import JiraIssue

class JiraIssueResolverTest(unittest.TestCase):
    def setUp(self) -> None:
        self.issue = JiraIssue('I am an issue', 'Bug', 'test-123')
        self.branch_creator = BranchCreator(self.issue, '/')

        return super().setUp()

    def test_it_returns_branch_type_bugfix_if_issue_is_a_bug(self):
        type = self.branch_creator.resolve_branch_type()

        self.assertEquals('bugfix', type)

    def test_it_returns_branch_type_feature_if_issue_is_not_a_bug(self):
        self.issue.type = 'Story'
        type = self.branch_creator.resolve_branch_type()

        self.assertEquals('feature', type)

    def test_it_includes_issue_key_in_branch_name(self):
        self.assertTrue('test-123' in self.branch_creator.get_branch_name())

    def test_it_formats_branch_name_using_type_key_and_issue_title(self):
        branch_name = self.branch_creator.get_branch_name()
        self.assertEquals(branch_name, 'bugfix/test-123-i-am-an-issue')

    def test_it_limits_issue_title_to_8_words(self):
        self.issue.title = 'Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit'
        branch_name = self.branch_creator.get_branch_name()
        self.assertEquals(branch_name, 'bugfix/test-123-neque-porro-quisquam-est-qui-dolorem-ipsum-quia')

    def test_it_removes_all_special_charters_from_title(self):
        self.issue.title = '*Neque ^porro &quisquam! est $qui? (dolorem) #ipsum... -quia+ dolor sit amet, consectetur, adipisci velit'
        branch_name = self.branch_creator.get_branch_name()
        self.assertEquals(branch_name, 'bugfix/test-123-neque-porro-quisquam-est-qui-dolorem-ipsum-quia')

    def test_it_strips_leading_and_trailing_whitespaces_from_jira_title(self):
        self.issue.title = '        Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit     '
        branch_name = self.branch_creator.get_branch_name()
        self.assertEquals(branch_name, 'bugfix/test-123-neque-porro-quisquam-est-qui-dolorem-ipsum-quia')

    @patch('os.chdir')
    def test_it_changes_directory_to_target_directory_if_defined(self, chdir_mock: Mock):        
        self.branch_creator.create_branch()

        chdir_mock.assert_called_once_with('/')

    @patch('os.chdir')
    def test_it_doesnt_change_directory_when_not_defined(self, chdir_mock: Mock):        
        self.branch_creator.application_directory = None
        self.branch_creator.create_branch()

        chdir_mock.assert_not_called()

    @patch('subprocess.call')
    def test_it_creates_local_git_branch_with_given_title(self, call_mock: Mock):
        self.branch_creator.application_directory = None
        self.branch_creator.create_branch()

        call_mock.assert_called_once_with(['git', 'checkout', '-b', 'bugfix/test-123-i-am-an-issue'])