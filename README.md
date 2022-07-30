# Jira Branch Creator
This is a simple command line application for creating local git branches using jira issue key and summary to keep track using jira, as well as making tracking tickets in your git easier by using the same names and summaries as the original jira tickets.

What this does is retrieve the issue metadata and navigate to your repository and checkout a local branch with the generated name

## Support
Currently Jira Branch Creator only works on *NIX systems, this includes MacOS and Linux, support for windows is not there yet

Tested on Ubuntu 22.04 and MacOS Monterey (12.5)

## Usage
To get up and running do the following:

1. clone the repository `git clone git@github.com:Abdul-fattah-Tayih/jira-branch-creator.git`
2. run `pip install -r requirements.txt`
3. run `python3 path/to/repo TICKET-KEY`
example: `python3 branch-creator TEST-123`

### Example
Let's say I have an issue of the type Story with the key `TEST-123`, and the title for that issue is: `As an admin, I want to be able to see login statistics for the users`, and I have a repository whose path is `~/code/my-repo`

Once we use the application, the `my-repo` repository will checkout a new local branch with the name: `feature/TEST-123-as-an-admin-i-want-to-be-able-to-see-login-statistics-for-the-users`

## Configuration
The app will ask you for variables, but to streamline the experience you can add the variables in your `~/.bashrc` or `~/.zshrc` file

### Variables
1. `jira_branch_creator_email`: The email or username of your account in jira
2. `jira_branch_creator_api_key`: The api key for your jira account, you can create one [Here](https://id.atlassian.com/manage-profile/security/api-tokens)
3. `jira_branch_creator_jira_subdomain`: The subdomain of your jira organization, for example in jira web your issue url would look like this `https://your-organization.atlassian.net/browse/TEST-123`, and so the value of this would be `your-organization`
4. `jira_branch_creator_application_directory`: The path to your repository, for example: `~/code/my_repo`