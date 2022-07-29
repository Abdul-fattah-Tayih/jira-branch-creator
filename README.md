# Jira Branch Creator
This is a simple command line application for creating local git branches using jira issue key and summary to keep track using jira, as well as making tracking tickets in your git easier by using the same names and summaries as the original jira tickets.

What this does is retrieve the issue metadata and navigate to your repository and checkout a local branch with the generated name

## Usage
To get up and running do the following:

1. clone the repository
2. run `python3 path/to/repo TICKET-KEY`
example: `python3 branch-creator TEST-123`

## Configuration
The app will ask you for variables, but to streamline the experience you can add the variables in your `~/.bashrc` or `~/.zshrc` file

### Variables
1. `jira_branch_creator_email`: The email or username of your account in jira
2. `jira_branch_creator_api_key`: The api key for your jira account, you can create one [Here](https://id.atlassian.com/manage-profile/security/api-tokens)
3. `jira_branch_creator_jira_subdomain`: The subdomain of your jira organization, for example in jira web your issue url would look like this `https://your-organization.atlassian.net/browse/TEST-123`, and so the value of this would be `your-organization`
4. `jira_branch_creator_application_directory`: The path to your repository, for example: `~/code/my_repo`