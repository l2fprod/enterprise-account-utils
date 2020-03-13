#!/usr/bin/python3
import inspect
import os
import sys
import json
from jinja2 import Template

def get_script_dir(follow_symlinks=True):
  path = inspect.getabsfile(get_script_dir)
  if follow_symlinks:
    path = os.path.realpath(path)
  return os.path.dirname(path)

with open('accounts.json', 'r') as accountsFile:
  accounts = json.load(accountsFile)

with open('account-groups.json', 'r') as groupsFile:
  groups = json.load(groupsFile)

with open(get_script_dir() + '/json2gv-styling.json', 'r') as styleFile:
  styles = json.load(styleFile)

with open(get_script_dir() + '/json2gv.j2', 'r') as templateFile:
  template = Template(templateFile.read())

# find the Enterprise account
for account in accounts:
  if account['is_enterprise_account'] is True:
    del account['parent']
    enterpriseAccount = account['crn']

# set it as the parent to all accounts currently linked to the enterprise
for account in accounts:
  if account.get('parent') and account['parent'].endswith(account['enterprise_id']):
    account['parent'] = enterpriseAccount

for group in groups:
  if group['parent'].endswith(group['enterprise_id']):
    group['parent'] = enterpriseAccount

# generate one graphviz per vpc
with open('enterprise.gv', 'w') as allOutputFile:
  allOutputFile.write(template.render(accounts=accounts, groups=groups, styles=styles))