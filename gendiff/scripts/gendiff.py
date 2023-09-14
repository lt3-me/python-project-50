from gendiff import generate_diff
from gendiff.console import get_arguments_from_input


def main():
    args = get_arguments_from_input()
    diff = generate_diff(*args)
    print(diff)
