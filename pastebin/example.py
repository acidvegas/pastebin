#!/usr/bin/env python
# PasteBin API Class - Developed by acidvegas in Python (https://acid.vegas/pastebin)

import getpass

import pastebin

# API Settings
api_dev_key  = 'CHANGEME'
api_user_key = None

# Define API
if api_user_key:
	api = pastebin.PasteBin(api_dev_key, api_user_key)
else:
	api = pastebin.PasteBin(api_dev_key)
	username = input('[?] - Username: ')
	password = getpass.getpass('[?] - Password: ')
	api_user_key = api.create_user_key(username, password)
	if 'Bad API request' not in api_user_key:
		print('[+] - You API user key is: ' + api_user_key)
		api = pastebin.PasteBin(api_dev_key, api_user_key)
	else:
		raise SystemExit('[!] - Failed to create API user key! ({0})'.format(api_user_key.split(', ')[1]))

# Create a Paste
data   = open(__file__).read()
result = api.paste(data, guest=True, name='Example Script', format='Python', private='1', expire='10M')
if 'Bad API request' not in result:
	print('[+] - PasteBin URL: ' + result)
else:
	raise SystemExit('[!] - Failed to create paste! ({0})'.format(api_user_key.split(', ')[1]))