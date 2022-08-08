# Jira Branch Creator
![Screenshot from 2022-08-08 20-07-27](https://user-images.githubusercontent.com/47541643/183474569-cc5b1c3e-62c9-4d17-893f-f04c59d6d213.png)

This is a simple command line application for creating local git branches using jira issue key and summary to keep track using jira, as well as making tracking tickets in your git easier by using the same names and summaries as the original jira tickets.

What this does is retrieve the issue metadata and navigate to your repository and checkout a local branch with the generated name

## Installation
Jira Branch Creator works on python 3.5+

Make sure to upgrade pip to the latest version

```shell 
pip3 install --upgrade pip
```

if you're using zsh on ubuntu make sure your path includes the local bin path, for example if your user is called `test_user` then your path should include it, so you can edit your rc file `nano ~/.zshrc` or `nano ~/.bashrc` and add this line

```bash
export PATH="/home/test_user/.local/bin:$PATH"
```

To get up and running do the following:

1. clone the repository `git clone git@github.com:Abdul-fattah-Tayih/jira-branch-creator.git`
2. navigate to the `jira-branch-creator` directory
3. run `pip install -r requirements.txt`
4. run `pip install .`

## Support
Currently Jira Branch Creator only works on *NIX systems, this includes MacOS and Linux, support for windows is not there yet

Tested on Ubuntu 22.04 and MacOS Monterey (12.5)

## Usage
run `jira-branch-creator ISSUE_KEY JIRA_USERNAME JIRA_API_KEY JIRA_SUBDOMAIN` in the directory of repository you want to use

you can use `jira-branch-creator --help` to get more information

### Usage Examples
Let's say I have an issue of the type Story with the key `TEST-123`, and the title for that issue is: `As an admin, I want to be able to see login statistics for the users`, and I have a repository whose path is `~/code/my-repo`

What i would do is the following:
```bash
cd ~/code/my-repo
jira-branch-creator TEST-123 my@email.com api_key my-organization
```
Once we use the application, the `my-repo` repository will checkout a new local branch with the name: `feature/TEST-123-as-an-admin-i-want-to-be-able-to-see-login-statistics-for-the-users`

## Configuration
The app will ask you for variables, but to streamline the experience you can add the variables in your `~/.bashrc` or `~/.zshrc` file

### Variables
1. `jira_branch_creator_email`: The email or username of your account in jira
2. `jira_branch_creator_api_key`: The api key for your jira account, you can create one [Here](https://id.atlassian.com/manage-profile/security/api-tokens)
3. `jira_branch_creator_jira_subdomain`: The subdomain of your jira organization, for example in jira web your issue url would look like this `https://your-organization.atlassian.net/browse/TEST-123`, and so the value of this would be `your-organization`

Open your rc file `nano ~/.bashrc` or `nano ~/.zshrc`

And paste this code block, replacing the values you need
```bash
export jira_branch_creator_email="your_jira_email@email.com"
export jira_branch_creator_api_key="your_jira_api_key"
export jira_branch_creator_jira_subdomain="your_organization_subdomain"
```

## Roadmap
- [x] alpha release: create branches locally
- [x] unit testing
- [x] improve experience
    - [x] add word limit option
    - [x] add arguments for required variables
    - [x] call app with name instead of `python3 path`
- [ ] Simplify configuration
- [ ] Add optional arguements to command to avoid tinkering with env
- [ ] Support Windows
- [ ] Add application to brew and apt
