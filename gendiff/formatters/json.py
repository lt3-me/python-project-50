import json


def format(diff):
    json_string = json.dumps(diff)
    return json_string
