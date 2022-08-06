import os
import click
from colorama import Fore, init
from services.branches import BranchService

def has_env(env_variable) -> bool:
    return env_variable in os.environ

@click.command()
@click.argument('issue_key', required=True)
@click.argument('jira_username', required=has_env('jira_branch_creator_email'), default=os.getenv('jira_branch_creator_email'))
@click.argument('jira_api_key', required=has_env('jira_branch_creator_api_key'), default=os.getenv('jira_branch_creator_api_key'))
@click.argument('jira_subdomain', required=has_env('jira_branch_creator_jira_subdomain'), default=os.getenv('jira_branch_creator_jira_subdomain'))
@click.option('--target-dir', default=os.curdir, help='The target directory, defaults to the current directory')
@click.option('--branch-word-limit', default=8, help='Limit the words of the branch name, default is 8, you can use -1 to include the entire issue name in the branch')
@click.option('--branch-type', help='By default jira-branch-creator resolves issues to feature/branch or bugfix/branch, you can override that here')
def cli(
        issue_key: str,
        jira_username: str,
        jira_api_key: str,
        jira_subdomain: str,
        target_directory: str,
        branch_word_limit: int,
        branch_type: str
    ):
    """
        Checkout a local branch that is corresponding with a jira issue
        
        ISSUE_KEY: your jira issue key, eg (TEST-123)

        JIRA_USERNAME: Your jira username or email that you use to login
        
        JIRA_API_KEY: Jira API key for your account, can obtained from https://id.atlassian.com/manage-profile/security/api-tokens

        JIRA_SUBDOMAIN: your organization subdomain in jira, eg https://my-organization.atlassian.net/browse/TEST-123)
    """

    init()

    service = BranchService(
        jira_username,
        jira_api_key,
        issue_key,
        jira_subdomain,
        target_directory
    )
    service.create_branch()