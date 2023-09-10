import json


def format(dict1, dict2, diff):
    for key in diff:
        if diff[key] == 'added' or diff[key] == 'unchanged':
            if isinstance(dict2[key], dict):
                diff[key] = unpack_nested_with_status(dict2[key], diff[key])
        elif diff[key] == 'removed':
            if isinstance(dict1[key], dict):
                diff[key] = unpack_nested_with_status(dict1[key], diff[key])
    json_string = json.dumps(diff)
    return json_string


def unpack_nested_with_status(dict_, status):
    unpacked = {}
    for key, value in dict_.items():
        if isinstance(value, dict):
            unpacked[key] = unpack_nested_with_status(value, status)
        else:
            unpacked[key] = status
    return unpacked
