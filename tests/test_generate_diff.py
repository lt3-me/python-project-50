from gendiff import generate_diff
import pytest
from os import path


def get_fixture_filepath(filename):
    return path.join(path.dirname(__file__), 'fixtures', filename)


file1j = get_fixture_filepath('file1.json')
file2j = get_fixture_filepath('file2.json')
file1y = get_fixture_filepath('file1.yaml')
file2y = get_fixture_filepath('file2.yml')
diff_result_file_stylish = get_fixture_filepath(
    'test_diff_result_stylish.txt')
diff_same_result_file_stylish = get_fixture_filepath(
    'test_same_result_stylish.txt')
diff_result_file_plain = get_fixture_filepath(
    'test_diff_result_plain.txt')
diff_result_file_json = get_fixture_filepath(
    'test_diff_result_json.txt')
diff_same_result_file_json = get_fixture_filepath(
    'test_same_result_json.txt')


def get_results(style):
    if style == 'stylish':
        with open(diff_result_file_stylish, "r") as f:
            result = f.read()
        with open(diff_same_result_file_stylish, "r") as f:
            result_same = f.read()
    elif style == 'plain':
        with open(diff_result_file_plain, "r") as f:
            result = f.read()
        result_same = ''
    elif style == 'json':
        with open(diff_result_file_json, "r") as f:
            result = f.read()
        with open(diff_same_result_file_json, "r") as f:
            result_same = f.read()
    else:
        raise Exception('Wrong formatting style')
    return result, result_same


styles = ('stylish', 'plain', 'json')
test_inputs = [(file1j, file2j), (file1y, file2y)]


@pytest.mark.parametrize(
    "input1, input2, style",
    [(i1, i2, style) for i1, i2 in test_inputs for style in styles])
def test_diff(input1, input2, style):
    expected, expected_same = get_results(style)
    assert generate_diff(input1, input2, style) == expected
    assert generate_diff(input1, input1, style) == expected_same
