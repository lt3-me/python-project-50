from gendiff import generate_diff
import gendiff.formats.stylish as stylish
import gendiff.formats.plain as plain
from os import path

file1j = path.join(path.dirname(__file__), 'fixtures', 'file1.json')
file2j = path.join(path.dirname(__file__), 'fixtures', 'file2.json')
file1y = path.join(path.dirname(__file__), 'fixtures', 'file1.yaml')
file2y = path.join(path.dirname(__file__), 'fixtures', 'file2.yml')

diff_result_file_stylish = path.join(path.dirname(__file__), 'fixtures',
                                     'test_diff_result_stylish.txt')
diff_same_result_file_stylish = path.join(path.dirname(__file__), 'fixtures',
                                          'test_same_result_stylish.txt')
diff_result_file_plain = path.join(path.dirname(__file__), 'fixtures',
                                   'test_diff_result_plain.txt')
diff_same_result_file_plain = path.join(path.dirname(__file__), 'fixtures',
                                        'test_same_result_plain.txt')

with open(diff_result_file_stylish, "r") as f:
    result_s = f.read()
with open(diff_result_file_plain, "r") as f:
    result_p = f.read()
with open(diff_same_result_file_stylish, "r") as f:
    result_same_s = f.read()
with open(diff_same_result_file_plain, "r") as f:
    result_same_p = f.read()


def test_diff_json_stylish():
    assert generate_diff(file1j, file2j, stylish.format) == result_s


def test_diff_json_plain():
    assert generate_diff(file1j, file2j, plain.format) == result_p


def test_diff_json_same_stylish():
    assert generate_diff(file1j, file1j, stylish.format) == result_same_s


def test_diff_json_same_plain():
    assert generate_diff(file1j, file1j, plain.format) == result_same_p


def test_diff_yaml_stylish():
    assert generate_diff(file1y, file2y, stylish.format) == result_s


def test_diff_yaml_plain():
    assert generate_diff(file1y, file2y, plain.format) == result_p


def test_diff_yaml_same_stylish():
    assert generate_diff(file1y, file1y, stylish.format) == result_same_s


def test_diff_yaml_same_plain():
    assert generate_diff(file1y, file1y, plain.format) == result_same_p
