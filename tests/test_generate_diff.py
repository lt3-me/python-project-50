from gendiff import generate_diff
import pytest
from os import path


def get_fixture_filepath(filename):
    return path.join(path.dirname(__file__), 'fixtures', filename)


def get_results(style):
    if style == 'stylish':
        diff_result_file_stylish = get_fixture_filepath(
            'test_diff_result_stylish.txt')
        diff_same_result_file_stylish = get_fixture_filepath(
            'test_same_result_stylish.txt')
        with open(diff_result_file_stylish, "r") as f:
            result = f.read()
        with open(diff_same_result_file_stylish, "r") as f:
            result_same = f.read()
    elif style == 'plain':
        diff_result_file_plain = get_fixture_filepath(
            'test_diff_result_plain.txt')
        with open(diff_result_file_plain, "r") as f:
            result = f.read()
        result_same = ''
    elif style == 'json':
        diff_result_file_json = get_fixture_filepath(
            'test_diff_result_json.txt')
        diff_same_result_file_json = get_fixture_filepath(
            'test_same_result_json.txt')
        with open(diff_result_file_json, "r") as f:
            result = f.read()
        with open(diff_same_result_file_json, "r") as f:
            result_same = f.read()
    else:
        raise Exception('Wrong formatting style')
    return result, result_same


file_name_inputs = [('file1.json', 'file2.json'), ('file1.yaml', 'file2.yml')]
styles = ('stylish', 'plain', 'json')


@pytest.mark.parametrize(
    "input1, input2, style",
    [(i1, i2, style) for i1, i2 in file_name_inputs for style in styles])
def test_diff(input1, input2, style):
    file1 = get_fixture_filepath(input1)
    file2 = get_fixture_filepath(input2)
    expected, expected_same = get_results(style)
    assert generate_diff(file1, file2, style) == expected
    assert generate_diff(file1, file1, style) == expected_same
