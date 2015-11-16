# coding: utf-8

import ConfigParser

config = ConfigParser.ConfigParser()
config.readfp(open(r'config'))

repository = config.get('git', 'repository')
user = config.get('git', 'username')
password = config.get('git', 'password')
token = config.get('git', 'token')
organization = config.get('git', 'organization')

from github import Github

g = Github(login_or_token=token)

org_list = g.get_user().get_orgs()


for org in org_list:
    if org.login == 'SteelSeries':
        repo = org.get_repo(repository)
        break

print repo
