from gendiff import generate_diff
from os import path

file1j = path.join(path.dirname(__file__), 'fixtures', 'file1.json')
file2j = path.join(path.dirname(__file__), 'fixtures', 'file2.json')
file1y = path.join(path.dirname(__file__), 'fixtures', 'file1.yaml')
file2y = path.join(path.dirname(__file__), 'fixtures', 'file2.yml')


def test_diff_json():
    diff_result_file = path.join(path.dirname(__file__), 'fixtures',
                                 'test_diff_result.txt')
    with open(diff_result_file, "r") as f:
        result = f.read()
    assert generate_diff(file1j, file2j) == result


def test_diff_json_same():
    diff_same_result_file = path.join(path.dirname(__file__), 'fixtures',
                                      'test_same_result.txt')
    with open(diff_same_result_file, "r") as f:
        result = f.read()
    assert generate_diff(file1j, file1j) == result


def test_diff_yaml():
    diff_result_file = path.join(path.dirname(__file__), 'fixtures',
                                 'test_diff_result.txt')
    with open(diff_result_file, "r") as f:
        result = f.read()
    assert generate_diff(file1y, file2y) == result


def test_diff_yaml_same():
    diff_same_result_file = path.join(path.dirname(__file__), 'fixtures',
                                      'test_same_result.txt')
    with open(diff_same_result_file, "r") as f:
        result = f.read()
    assert generate_diff(file1y, file1y) == result
