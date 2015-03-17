import os, json, requests, sys
import parser_helper
import config
from requests.auth import HTTPBasicAuth

args = sys.argv
builder = None
commit_id = None

# Get build info arguments
if (len(args) == 3):
	builder = args[1]
	commit_id = args[2]	

# Gets output template. This will include build information if it is given
json_tests = parser_helper.getJsonTemplate(builder, commit_id)

os.chdir(config.RESULTS_PATH)

# Step through the directory with the output json files
for root, dirs, files in os.walk('.'):
	for jsonFile in files:
		test = parser_helper.openJSON(jsonFile)
		json_tests["tests"].append(test) 

# Get username and pw for authentication
json_data = open(config.PATH,'r')
data = json.load(json_data)
json_data.close()

headers = {'content-type': 'application/json'}
url = config.URL


# Send post request
r = requests.post(url, data=json.dumps(json_tests), headers=headers, 
	auth=HTTPBasicAuth(data['username'], data['pw']))

# Print the status
print "Request status = " + str(r.status_code)
print r.text
