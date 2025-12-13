#Storing data using Json
#Json(Java Script Object Notation)

#Using Json Loads and Json Dumps

#The first program will use a Json dumps to store a set of numbers
from pathlib import Path
import json
def jsonDumpFunc():
    numbers = [2, 3, 4 ,11, 23]

    filePath = Path(r"Chapter 10 - Files and Exceptions\numbers.json")

    #json.dumps returns a json formated string value to contents which is then written to 
    # a file
    contents = json.dumps(numbers)

    #we have the location we want to write to and the contents we use the method
    #write_text on the loction to write the contents which we got from
    #json.dumps method
    filePath.write_text(contents)

    #utilizing json loads to read data from a json file the one we just made specificaly

def jsonLoadsFunc():
    filePath = Path(r"Chapter 10 - Files and Exceptions\numbers.json")
    contents = filePath.read_text()
    numbers = json.loads(contents)

    print(numbers)

jsonLoadsFunc()