from setuptools import setup

setup(
    name='jira-branch-creator',
    version='0.2.0',
    py_modules=['jira-branch-creator'],
    install_requires=[
        'Click',
        'Colorama',
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'jira-branch-creator=jira_branch_creator:cli',
        ],
    },
)