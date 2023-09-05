from gendiff.parsing import parse_file
import gendiff.formats.stylish as stylish


def generate_diff(file_path1, file_path2, format_func=stylish.format):
    file1 = parse_file(file_path1)
    file2 = parse_file(file_path2)

    def gendiff(file1, file2):
        diff = {}
        keys_set1 = set(file1.keys())
        keys_set2 = set(file2.keys())
        combined_keys_set = sorted(keys_set1.union(keys_set2))
        for key in combined_keys_set:
            comp_result = compare_by_key(file1, file2, key)
            if comp_result == 'replaced':
                if isinstance(file1[key], dict) and \
                     isinstance(file2[key], dict):
                    comp_result = gendiff(file1[key], file2[key])
            diff[key] = comp_result
        return diff

    diff = gendiff(file1, file2)

    return format_func(file1, file2, diff)


def compare_by_key(dict1, dict2, key):
    entry1 = dict1.get(key, KeyError)
    entry2 = dict2.get(key, KeyError)
    if entry1 is KeyError:
        return ('added')
    if entry2 is KeyError:
        return ('removed')
    if entry1 == entry2:
        return ('unchanged')
    else:
        return ('replaced')
