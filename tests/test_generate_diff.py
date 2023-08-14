from gendiff import generate_diff
from os import path

file1 = path.join(path.dirname(__file__), 'fixtures', 'file1.json')
file2 = path.join(path.dirname(__file__), 'fixtures', 'file2.json')


def test_diff():
    diff_result_file = path.join(path.dirname(__file__), 'fixtures',
                                 'test_diff_result.txt')
    with open(diff_result_file, "r") as f:
        result = f.read()
    assert generate_diff(file1, file2) == result


def test_diff_same():
    diff_same_result_file = path.join(path.dirname(__file__), 'fixtures',
                                      'test_same_result.txt')
    with open(diff_same_result_file, "r") as f:
        result = f.read()
    assert generate_diff(file1, file1) == result
