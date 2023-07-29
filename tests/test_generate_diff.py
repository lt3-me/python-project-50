from gendiff import generate_diff
from os import path

file1 = path.join(path.dirname(__file__), 'fixtures', 'file1.json')
file2 = path.join(path.dirname(__file__), 'fixtures', 'file2.json')


def test_diff():
    assert generate_diff(file1, file2) == '''\
{
  - follow: False
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: True
}'''


def test_diff_same():
    assert generate_diff(file1, file1) == '''\
{
    follow: False
    host: hexlet.io
    proxy: 123.234.53.22
    timeout: 50
}'''
