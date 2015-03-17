# ChronoTest_Parser
Parser for all tests in chrono.

Setup:

The only dependency the parser has is the requests python library. It can be downloaded
from here: http://docs.python-requests.org/en/latest/

or just run:
```
pip install requests
```

After doing that folow these steps:

1. Rename config_example.py to config.py
2. Change the PATH variable to the path to a json file that contains authentication information. The json file should look like this:
```
{
username: "SAMPLE USERNAME"
pw: "THE PASSWORD"
}
```
3. Change the URL variable to the API url. In my case when I run locally this path looks like this:
```
URL = 'http://localhost:5000/chrono_test/api/tests'
```
4. Finally change RESULTS_PATH in config.py to the path to the folder where all the results json files are saved. In my case this looks like this
```
RESULTS_PATH = '../results'
```

Now you should be all set to run 

```
python parser.py
```

and push your results to the database. You can also give the scripts 2 arguments the builder and the commit id:
```
python parser.py builder commit_id
```

