import os, json, requests
import json_helper
from config import PATH
from requests.auth import HTTPBasicAuth


json_tests = json_helper.getJsonTemplate()

os.chdir("json")
counter = 0

for root, dirs, files in os.walk('.'):

	for jsonFile in files:

		print jsonFile
		test = json_helper.openJSON(jsonFile)
		json_tests["tests"].append(test) 
		counter = counter

print json.dumps(json_tests, indent = 4) 

json_data = open(PATH,'r')
data = json.load(json_data)
json_data.close()

headers = {'content-type': 'application/json'}
url = "http://localhost:5000/chrono_test/api/tests"

r = requests.post(url, data=json.dumps(json_tests), headers=headers, 
	auth=HTTPBasicAuth(data['username'], data['pw']))

print "Request status = " + str(r.status_code)
