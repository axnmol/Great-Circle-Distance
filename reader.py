import json

VALID_FIELDS = ["latitude", "id", "longitude"]
CONNECTIONS = ["start","end"]

def readloc(filename):
    with open(filename) as json_file:
        try:
            data = json.load(json_file)
        except json.JSONDecodeError as ex:
            print("Malformed data: {}".format(ex.msg))
        
        for p in data:
            if all([field in p for field in VALID_FIELDS]):
                yield p
            else:
                print("Missing field in data. Valid fields are {}".format(", ".join(VALID_FIELDS)))

def readpaths(filename):
    with open(filename) as json_file:
        try:
            data = json.load(json_file)
        except json.JSONDecodeError as ex:
            print("Malformed data: {}".format(ex.msg))
        
        for p in data:
            if all([field in p for field in CONNECTIONS]):
                yield p
            else:
                print("Missing field in data. Valid fields are {}".format(", ".join(VALID_FIELDS)))