from gendiff.parsing import get_dict_from_file
from gendiff.comparing import get_difference
from gendiff.formatters import get_format_function_from_str


def generate_diff(file_path1, file_path2, format='stylish'):
    file1 = get_dict_from_file(file_path1)
    file2 = get_dict_from_file(file_path2)
    format_func = get_format_function_from_str(format)

    diff = get_difference(file1, file2)
    return format_func(diff)
