import json


def generate_diff(file_path1, file_path2):
    file1 = json.load(open(file_path1))
    file2 = json.load(open(file_path2))

    keys_set1 = set(file1.keys())
    keys_set2 = set(file2.keys())
    combined_keys_set = sorted(keys_set1.union(keys_set2))
    diff = ''.join(map(compare_by_key, combined_keys_set))
    return '{\n' + diff + '}'


def compare_by_key(dict1, dict2, key):
    entry1 = dict1.get(key, KeyError)
    entry2 = dict2.get(key, KeyError)
    if entry1 is KeyError:
        return (f'    + {key}: {entry2}\n')
    if entry2 is KeyError:
        return (f'    - {key}: {entry1}\n')

    if entry1 == entry2:
        return (f'      {key}: {entry1}\n')
    else:
        return (f'    - {key}: {entry1}\n    + {key}: {entry2}\n')
