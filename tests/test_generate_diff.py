from gendiff import generate_diff
import pytest
from os import path


def get_parameters():
    file_name_inputs = [('file1.json', 'file2.json'),
                        ('file1.yaml', 'file2.yml')]
    styles = ('stylish', 'plain', 'json')
    results_diff = ('test_diff_result_stylish.txt',
                    'test_diff_result_plain.txt',
                    'test_diff_result_json.txt')
    results_same = ('test_same_result_stylish.txt',
                    'test_same_result_plain.txt',
                    'test_same_result_json.txt')
    parameters_diff = [(i1, i2, result_filename, style)
                       for i1, i2 in file_name_inputs
                       for style, result_filename in zip(styles, results_diff)]
    parameters_same = [(i1, i1, result_filename, style)
                       for i1, _ in file_name_inputs
                       for style, result_filename in zip(styles, results_same)]
    return parameters_diff + parameters_same


def get_fixture_filepath(filename):
    return path.join(path.dirname(__file__), 'fixtures', filename)


@pytest.mark.parametrize(
    "input1, input2, expected_filename, style", get_parameters())
def test_diff(input1, input2, expected_filename, style):
    file1 = get_fixture_filepath(input1)
    file2 = get_fixture_filepath(input2)
    with open(get_fixture_filepath(expected_filename), "r") as f:
        expected = f.read()
        assert generate_diff(file1, file2, style) == expected
