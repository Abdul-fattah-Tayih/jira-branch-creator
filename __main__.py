import os
import sys
from services.branches import BranchService

variables = {
    "jira_subdomain": None,
    "application_directory": None,
    "email": None,
    "api_key": None
}

for variable_name, variable_value in variables.items():
    env_name = f'jira_branch_creator_{variable_name}'

    if env_name not in os.environ:
        print(f'You can adding an environment variable with the name {env_name} to your ~/.zshrc or ~/.bashrc file to avoid adding this every time you run the command')
        variables[variable_name] = input(f'Please enter the value for {variable_name}: ')
    else:
        variables[variable_name] = os.environ[env_name]

if len(sys.argv) < 2:
    variables['issue_key'] = input('Enter issue key: ')
else:
    variables['issue_key'] = sys.argv[1]

service = BranchService(**variables)
service.create_branch()
