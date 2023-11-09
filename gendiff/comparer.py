def get_difference(file1, file2):
    diff = {}
    keys_set1 = set(file1.keys())
    keys_set2 = set(file2.keys())

    keys_added = keys_set2 - keys_set1
    keys_removed = keys_set1 - keys_set2
    keys_in_both_sets = keys_set1.intersection(keys_set2)

    for key in keys_added:
        node = file2.get(key, object)
        diff[key] = {'status': 'added', 'value': node}

    for key in keys_removed:
        node = file1.get(key, object)
        diff[key] = {'status': 'removed', 'value': node}

    for key in keys_in_both_sets:
        node1 = file1.get(key, object)
        node2 = file2.get(key, object)

        if node1 == node2:
            diff[key] = {'status': 'unchanged', 'value': node1}
        elif isinstance(node1, dict) and isinstance(node2, dict):
            diff[key] = {'status': 'nested',
                         'children': get_difference(node1, node2)}
        else:
            diff[key] = {'status': 'updated',
                         'value': node2, 'old_value': node1}

    return dict(sorted(diff.items()))
