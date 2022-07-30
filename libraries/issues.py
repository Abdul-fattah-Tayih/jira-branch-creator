import json
from colorama import Fore
import requests
from requests.auth import HTTPBasicAuth

class JiraIssue:
    TYPE_STORY = 'Story'
    TYPE_BUG = 'Bug'

    def __init__(self, title: str, type: str, key: str) -> None:
        self.title = title
        self.type = type
        self.key = key

    def is_bug(self) -> bool:
        return self.type == JiraIssue.TYPE_BUG

    def is_story(self) -> bool:
        return self.type == JiraIssue.TYPE_STORY

class JiraIssueResolver:
    API_ENDPOINT_TEMPLATE = "https://{0}.atlassian.net/rest/api/3/issue/{1}"

    def __init__(self, jira_subdomain, issue_key, email, api_key) -> None:
        self.jira_subdomain = jira_subdomain
        self.issue_key = issue_key
        self.email = email
        self.api_key = api_key

    def retrieve(self) -> JiraIssue:
        auth = HTTPBasicAuth(self.email, self.api_key)
        headers = {
            "Accept": "application/json"
        }

        response = requests.request(
            "GET",
            f'{JiraIssueResolver.API_ENDPOINT_TEMPLATE.format(self.jira_subdomain ,self.issue_key)}?fields=summary,issuetype',
            headers=headers,
            auth=auth
        )

        if response.status_code != 200:
            print(f'{Fore.RED} Request failed for {self.issue_key}, error: {response.reason}')
            exit()

        response_json = json.loads(response.text)
        
        return JiraIssue(response_json['fields']['summary'], response_json['fields']['issuetype']['name'], response_json['key'])