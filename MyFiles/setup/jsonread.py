import json

def json_read(file):
    with open(file, 'r') as myfile:
        data = myfile.read()

    my_vars = json.loads(data)

    # print(str(obj['uname']))

    return my_vars
