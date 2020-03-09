import json

FILE = "variables.json"


def json_read():
    with open(FILE, 'r') as myfile:
        data = myfile.read()

    my_vars = json.loads(data)

    # print(str(my_vars['uname']))
    myfile.close()
    return my_vars


def changeJson(string, key):
    with open(FILE, 'r+') as writeFile:
        data = json.load(writeFile)
        data[key] = string
        writeFile.seek(0)
        json.dump(data, writeFile)
        writeFile.truncate()
        writeFile.close()
