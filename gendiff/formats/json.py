import json


def format(dict1, dict2, diff):
    for key in diff:
        if diff[key] == 'added' or diff[key] == 'unchanged':
            dict_ = dict2
        elif diff[key] == 'removed':
            dict_ = dict1
        else:
            continue
        if isinstance(dict_[key], dict):
            diff[key] = unpack_nested_with_status(dict_[key], diff[key])
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
