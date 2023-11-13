def get_difference(dict1, dict2):
    diff = {}
    keys_set1 = set(dict1.keys())
    keys_set2 = set(dict2.keys())

    keys_added = keys_set2 - keys_set1
    keys_removed = keys_set1 - keys_set2
    all_keys = keys_set1.union(keys_set2)

    for key in all_keys:
        node1 = dict1.get(key, object)
        node2 = dict2.get(key, object)

        if node1 == node2:
            diff[key] = {'status': 'unchanged', 'value': node1}
        elif key in keys_added:
            node = dict2.get(key, object)
            diff[key] = {'status': 'added', 'value': node}
        elif key in keys_removed:
            node = dict1.get(key, object)
            diff[key] = {'status': 'removed', 'value': node}
        elif isinstance(node1, dict) and isinstance(node2, dict):
            diff[key] = {'status': 'nested',
                         'children': get_difference(node1, node2)}
        else:
            diff[key] = {'status': 'updated',
                         'value': node2, 'old_value': node1}

    return dict(sorted(diff.items()))
