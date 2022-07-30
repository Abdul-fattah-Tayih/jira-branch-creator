import os, re
import subprocess

from colorama import Fore
from libraries.issues import JiraIssue

class BranchCreator:
    def __init__(self, application_directory: str, jira_issue: JiraIssue) -> None:
        self.application_directory = application_directory
        self.jira_issue = jira_issue

    def resolve_branch_type(self) -> str:
        return 'bugfix' if self.jira_issue.is_bug() else 'feature'

    def normalize_title(self) -> str:
        title = self.jira_issue.title
        title = title.lower().replace(" ", "-")
        title = re.sub('[^a-zA-Z0-9 \-\n\.]', '', title)

        return title

    def create_branch(self) -> None:
        try:
            os.chdir(os.path.expanduser(self.application_directory))
        except FileNotFoundError:
            print(f'{Fore.RED} Application directory ({self.application_directory}) is invalid, terminating.')
            exit()

        branch_name = f'{self.resolve_branch_type()}/{self.jira_issue.key}-{self.normalize_title()}'
        subprocess.call(['git', 'checkout', '-b', branch_name])
