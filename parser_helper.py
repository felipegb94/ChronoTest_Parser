import json, socket

#Required keys in the json file
keys = ["name", "project_name", "metrics", "execution_time", "passed"]

'''
Opens, validates and returns a json file
'''
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

'''	
Creates a json object as input and creates a json file with that object.
'''
def getJSON(json_data, filename):
	with open(filename, 'w') as outfile:
		json.dump(json_data, outfile, indent = 4)

'''
Validate that the input json file contains the required keys.
'''
def validateJSON(data):

	for key in keys:
		if(not key in data):
			raise Exception("Invalid JSON format: Make sure your JSON file contains required fields. ")

	print "Valid JSON."

'''
Returns the template to fill with tests. The template comes with the build
information of the current machine.
'''
def getJsonTemplate(builder = None, commit_id = None):

	config = getConfig(builder, commit_id)
	tests = []
	template = {u"config" : config,
			  	u"tests" : tests,
				}
				
	return template

'''
Returns the config information for the template
'''
def getConfig(builder = None, commit_id = None):

	repos_commitID = builder
	build_builder = commit_id

	# Get hostname
	build_hostname = socket.gethostname()


	repos_data = {u"commitID" : repos_commitID}

	build_info = {u"hostname" : build_hostname,
				  u"builder" : build_builder
			  	  }

	config = {u"build_info" : build_info,
			   u"repos_data" : repos_data
			   }
	return config

