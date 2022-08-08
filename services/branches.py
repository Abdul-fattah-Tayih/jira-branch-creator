from typing import Optional
from libraries.git import BranchCreator
from libraries.issues import JiraIssueResolver

class BranchService:
    def __init__(self, email: str, api_key: str, issue_key: str, jira_subdomain: str, application_directory: str, branch_word_limit: Optional[str] = None, branch_type: Optional[str] = None) -> None:
        self.email = email
        self.api_key = api_key
        self.application_directory = application_directory
        self.issue_key = issue_key
        self.jira_subdomain = jira_subdomain
        self.branch_word_limit = branch_word_limit
        self.branch_type = branch_type

    def create_branch(self):
        jira_issue = JiraIssueResolver(self.jira_subdomain, self.issue_key, self.email, self.api_key).resolve()
        branch_creator = BranchCreator(jira_issue, self.application_directory, self.branch_word_limit, self.branch_type)
        branch_creator.create_branch()