import os
import subprocess
from libraries.git import BranchCreator
from libraries.issues import JiraIssueResolver

class BranchService:
    def __init__(self, email: str, api_key: str, issue_key: str, jira_subdomain: str, application_directory: str) -> None:
        self.email = email
        self.api_key = api_key
        self.application_directory = application_directory
        self.issue_key = issue_key
        self.jira_subdomain = jira_subdomain

    def create_branch(self):
        jira_issue = JiraIssueResolver(self.jira_subdomain, self.issue_key, self.email, self.api_key).retrieve()
        branch_creator = BranchCreator(self.application_directory, jira_issue)
        branch_creator.create_branch()