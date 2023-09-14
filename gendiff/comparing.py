def get_difference(file1, file2):
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
                'children': get_difference(node1, node2)}
    else:
        return {'status': 'updated', 'value': node2, 'old_value': node1}
