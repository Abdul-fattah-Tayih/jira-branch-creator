import os, re
import subprocess
from typing import Optional
from colorama import Fore
from libraries.issues import JiraIssue
from libraries.utilities import limit_words, slugify

class BranchCreator:
    def __init__(self, jira_issue: JiraIssue, application_directory: Optional[str] = None) -> None:
        self.application_directory = application_directory
        self.jira_issue = jira_issue

    def resolve_branch_type(self) -> str:
        return 'bugfix' if self.jira_issue.is_bug() else 'feature'

    def normalize_title(self) -> str:
        title = self.jira_issue.title
        title = re.sub('[^a-zA-Z0-9 \n]', '', title).strip()
        title = limit_words(title, 8)
        title = slugify(title)

        return title

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
