import json

#Required keys in the json file
keys = ["name", "project_name", "metrics", "execution_time", "passed"]

#Opens, validates and returns a json file
def openJSON(json_filename):
	try:
		json_data = open(json_filename, 'r')
	except IOError:
		print "The file specified does not exist."
		quit()

	data = json.load(json_data)
	json_data.close()
	validateJSON(data)

	return data
	
#Creates a json object as input and creates a json file with that object.
def getJSON(json_data, filename):
	with open(filename, 'w') as outfile:
		json.dump(json_data, outfile, indent = 4)

#Validate that the input json file contains the required keys.
def validateJSON(data):

	for key in keys:
		if(not key in data):
			raise Exception("Invalid JSON format: Make sure your JSON file contains required fields. ")

	print "Valid JSON."

def getJsonTemplate():
	config = getConfig()
	tests = []
	template = {u"config" : config,
			  	u"tests" : tests,
				}
				
	return template

def getTestTemplate():
	template = {u"name" : "",
			  	u"project_name" : "",
			  	u"passed" : False,
			  	u"runtime" : {u"runtimes": [],
			  				  u"runtime_values": []
			  				 }
				}
	return template

def getRuntimeJson(runtimes, runtime_values):
	runtimeJson = {}
	for index in range(len(runtimes)):
		key = runtimes[index]
		value = runtime_values[index]
		runtimeJson[key] = value
	return runtimeJson

def getConfig():
	project_name = "chrono"

	repos_url = "SampleURL"
	repos_branch = "sampleBranch"
	repos_commitID = "sampleID"
	repos_data = {u"url" : repos_url,
			  	  u"branch" : repos_branch,
			      u"commitID" : repos_commitID
			  	}

	build_hostname = "hostname1"
	build_builder = "SampleBuilder2"

	build_info = {u"hostname" : build_hostname,
				  u"builder" : build_builder
			  	}


	jsonObj = {u"project_name" : project_name,
			   u"build_info" : build_info,
			   u"repos_data" : repos_data
		   	}
	return jsonObj

