import os, re
import subprocess
from typing import Optional
from colorama import Fore
from libraries.issues import JiraIssue
from libraries.utilities import limit_words, slugify

class BranchCreator:
    DEFAULT_BRANCH_WORD_LIMIT = 8

    def __init__(self, jira_issue: JiraIssue, application_directory: Optional[str] = None, branch_word_limit: Optional[str] = None, branch_type: Optional[str] = None) -> None:
        self.application_directory = application_directory
        self.jira_issue = jira_issue
        self.branch_word_limit = branch_word_limit
        self.branch_type = branch_type

    def resolve_branch_type(self) -> str:
        if self.branch_type:
            return self.branch_type

        return 'bugfix' if self.jira_issue.is_bug() else 'feature'

    def normalize_title(self) -> str:
        title = self.jira_issue.title
        title = re.sub('[^a-zA-Z0-9 \n]', '', title).strip()

        if word_limit := self.get_branch_word_limit():
            title = limit_words(title, word_limit)

        title = slugify(title)

        return title

    def get_branch_word_limit(self) -> Optional[str]:
        if self.branch_word_limit == -1:
            return None
        elif self.branch_word_limit:
            return self.branch_word_limit

        return self.DEFAULT_BRANCH_WORD_LIMIT

    def get_branch_name(self):
        return f'{self.resolve_branch_type()}/{self.jira_issue.key}-{self.normalize_title()}'

    def create_branch(self) -> None:
        if self.application_directory:
            try:
                os.chdir(os.path.expanduser(self.application_directory))
            except FileNotFoundError:
                print(f'{Fore.RED} Application directory ({self.application_directory}) is invalid, terminating.')
                exit()

        branch_name = self.get_branch_name()
        subprocess.call(['git', 'checkout', '-b', branch_name])
