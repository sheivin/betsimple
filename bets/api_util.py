###
# Utility for api requests
###

import requests
from requests.exceptions import HTTPError

from datetime import date

api_key = "1859d7ee0c1c48e281dae70037aa66b4"

def connect(url):
	"""
	Make API call
	"""
	# print(url)
	headers = {'X-Auth-Token': api_key}
	response = requests.get(url, headers=headers)

	# print(response)

	if (response.status_code != 200):
		print('Status: ', response.status_code, 'Error occurred. Exiting...')
		exit()
	return response.json()



