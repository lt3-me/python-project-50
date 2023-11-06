def get_difference(file1, file2):
    diff = {}
    keys_set1 = set(file1.keys())
    keys_set2 = set(file2.keys())
    combined_keys_set = sorted(keys_set1.union(keys_set2))

    for key in combined_keys_set:
        node1 = file1.get(key, object)
        node2 = file2.get(key, object)

        if node1 == node2:
            diff[key] = {'status': 'unchanged', 'value': node1}
        elif node1 is object:
            diff[key] = {'status': 'added', 'value': node2}
        elif node2 is object:
            diff[key] = {'status': 'removed', 'value': node1}
        elif isinstance(node1, dict) and isinstance(node2, dict):
            diff[key] = {'status': 'updated',
                         'children': get_difference(node1, node2)}
        else:
            diff[key] = {'status': 'updated',
                         'value': node2, 'old_value': node1}

    return diff
