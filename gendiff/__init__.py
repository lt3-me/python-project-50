from gendiff.parser import get_dict_from_file
from gendiff.comparer import get_difference
from gendiff.formatters import get_formatted_diff


def generate_diff(file_path1, file_path2, format='stylish'):
    file1 = get_dict_from_file(file_path1)
    file2 = get_dict_from_file(file_path2)
    diff = get_difference(file1, file2)

    return get_formatted_diff(diff, format)
