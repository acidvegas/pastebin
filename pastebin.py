#!/usr/bin/env python
# PasteBin API Class - Developed by acidvegas in Python (https://git.acid.vegas/pastebin)

'''
API Documentation: https://pastebin.com/doc_api
'''

import urllib.parse
import urllib.request

class PasteBin:
	def __init__(self, api_dev_key, api_user_key=None):
		self.api_dev_key  = api_dev_key
		self.api_user_key = api_user_key

	def api_call(self, method, params):
		'''Make a call to the PasteBin API.'''
		response = urllib.request.urlopen('https://pastebin.com/api/' + method, urllib.parse.urlencode(params).encode('utf-8'), timeout=10)
		return response.read().decode()

	def create_user_key(self, username, password):
		'''Create a user key for the PasteBin API.'''
		params = {'api_dev_key':self.api_dev_key, 'api_user_name':username, 'api_user_password':password}
		return self.api_call('api_login.php', params)

	def paste(self, data, guest=False, name=None, format=None, private=None, expire=None):
		'''Create a paste on PasteBin.'''
		params = {'api_dev_key':self.api_dev_key, 'api_option':'paste', 'api_paste_code':data}
		if not guest : params['api_user_key']          = self.api_user_key
		if name      : params['api_paste_name']        = name
		if format    : params['api_paste_format']      = format
		if private   : params['api_paste_private']     = private
		if expire    : params['api_paste_expire_date'] = expire
		return self.api_call('api_post.php', params)

	def list_pastes(self, results_limit=None):
		'''List pastes created by the user.'''
		params = {'api_dev_key':self.api_dev_key, 'api_user_key':self.api_user_key, 'api_option':'list'}
		if results_limit:
			params['api_results_limit'] = results_limit
		return self.api_call('api_post.php', params)

	def trending_pastes(self):
		'''List trending pastes.'''
		params = {'api_dev_key':self.api_dev_key, 'api_option':'trends'}
		return self.api_call('api_post.php', params)

	def delete_paste(self, paste_key):
		'''Delete a paste.'''
		params = {'api_dev_key':self.api_dev_key, 'api_user_key':self.api_user_key, 'api_paste_key':paste_key, 'api_option':'delete'}
		return self.api_call('api_post.php', params)

	def user_info(self):
		'''Get information about the user.'''
		params = {'api_dev_key':self.api_dev_key, 'api_user_key':self.api_user_key, 'api_option':'userdetails'}
		return self.api_call('api_post.php', params)

	def raw_pastes(self, paste_key):
		'''Get the raw data of a paste.'''
		params = {'api_dev_key':self.api_dev_key, 'api_user_key':self.api_user_key, 'api_paste_key':paste_key, 'api_option':'show_paste'}
		return self.api_call('api_raw.php', params)