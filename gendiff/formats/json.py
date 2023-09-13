import json


def format(diff):
    json_string = json.dumps(diff)
    return json_string


# def unpack_nested_with_status(dict_, status):
#     unpacked = {}
#     for key, value in dict_.items():
#         if isinstance(value, dict):
#             unpacked[key] = unpack_nested_with_status(value, status)
#         else:
#             unpacked[key] = status
#     return unpacked
