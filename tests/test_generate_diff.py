from gendiff import generate_diff
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
diff_result_file_json = path.join(path.dirname(__file__), 'fixtures',
                                  'test_diff_result_json.txt')
diff_same_result_file_json = path.join(path.dirname(__file__), 'fixtures',
                                       'test_same_result_json.txt')

with open(diff_result_file_stylish, "r") as f:
    result_s = f.read()
with open(diff_result_file_plain, "r") as f:
    result_p = f.read()
with open(diff_result_file_json, "r") as f:
    result_j = f.read()
with open(diff_same_result_file_stylish, "r") as f:
    result_same_s = f.read()
with open(diff_same_result_file_json, "r") as f:
    result_same_j = f.read()
result_same_p = ''


def test_diff_stylish():
    assert generate_diff(file1j, file2j, 'stylish') == result_s
    assert generate_diff(file1y, file2y, 'stylish') == result_s
    assert generate_diff(file1j, file1j, 'stylish') == result_same_s
    assert generate_diff(file1y, file1y, 'stylish') == result_same_s


def test_diff_plain():
    assert generate_diff(file1j, file2j, 'plain') == result_p
    assert generate_diff(file1y, file2y, 'plain') == result_p
    assert generate_diff(file1j, file1j, 'plain') == result_same_p
    assert generate_diff(file1y, file1y, 'plain') == result_same_p


def test_diff_json():
    assert generate_diff(file1j, file2j, 'json') == result_j
    assert generate_diff(file1y, file2y, 'json') == result_j
    assert generate_diff(file1j, file1j, 'json') == result_same_j
    assert generate_diff(file1y, file1y, 'json') == result_same_j
