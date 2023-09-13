from gendiff.parsing import parse_file
import gendiff.formats.stylish as stylish


# def generate_diff(file_path1, file_path2, format_func=stylish.format):
#     file1 = parse_file(file_path1)
#     file2 = parse_file(file_path2)

#     def gendiff(file1, file2):
#         diff = {}
#         keys_set1 = set(file1.keys())
#         keys_set2 = set(file2.keys())
#         combined_keys_set = sorted(keys_set1.union(keys_set2))
#         for key in combined_keys_set:
#             comp_result = compare_by_key(file1, file2, key)
#             node = {'status': comp_result}
#             if comp_result == 'updated':
#                 if isinstance(file1[key], dict) and \
#                      isinstance(file2[key], dict):
#                     node['children'] = gendiff(file1[key], file2[key])
#                 else:
#                     node['value'] = file2[key]
#                     node['old_value'] = file1[key]
#             elif comp_result == 'added' or comp_result == 'unchanged':
#                 if isinstance(file2[key], dict):
#                     node['children'] = unpack_nested_with_status(
#                         file2[key], comp_result)
#                 else:
#                     node['value'] = file2[key]
#             elif comp_result == 'removed':
#                 if isinstance(file1[key], dict):
#                     node['children'] = unpack_nested_with_status(
#                         file1[key], comp_result)
#                 else:
#                     node['value'] = file1[key]
#             diff[key] = node
#         return diff

#     diff = gendiff(file1, file2)

#     return format_func(file1, file2, diff)

def generate_diff(file_path1, file_path2, format_func=stylish.format):
    file1 = parse_file(file_path1)
    file2 = parse_file(file_path2)
    diff = generate_difference(file1, file2)
    return format_func(diff)


def generate_difference(file1, file2):
    diff = {}
    keys_set1 = set(file1.keys())
    keys_set2 = set(file2.keys())
    combined_keys_set = sorted(keys_set1.union(keys_set2))

    for key in combined_keys_set:
        node = compare_values(file1.get(key, object),
                              file2.get(key, object))
        diff[key] = node

    return diff


def compare_values(node1, node2):
    if node1 == node2:
        return {'status': 'unchanged', 'value': node1}
    elif node1 is object:
        return {'status': 'added', 'value': node2}
    elif node2 is object:
        return {'status': 'removed', 'value': node1}
    elif isinstance(node1, dict) and isinstance(node2, dict):
        return {'status': 'updated',
                'children': generate_difference(node1, node2)}
    else:
        return {'status': 'updated', 'value': node2, 'old_value': node1}


# def compare_by_key(dict1, dict2, key):
#     entry1 = dict1.get(key, KeyError)
#     entry2 = dict2.get(key, KeyError)
#     if entry1 is KeyError:
#         return ('added')
#     if entry2 is KeyError:
#         return ('removed')
#     if entry1 == entry2:
#         return ('unchanged')
#     else:
#         return ('updated')


# def unpack_nested_with_status(dict_, status):
#     unpacked = {}
#     for key, value in dict_.items():
#         if isinstance(value, dict):
#             unpacked[key] = unpack_nested_with_status(value, status)
#         else:
#             unpacked[key] = status
#     return unpacked
