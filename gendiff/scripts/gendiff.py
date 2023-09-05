import argparse
from gendiff import generate_diff
import gendiff.formats.stylish as stylish


def main():
    parser = argparse.ArgumentParser(
                    prog='gendiff',
                    description='Compares two configuration files \
                        and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', type=str, default='stylish',
                        help='set format of output')
    args = parser.parse_args()
    if args.format == 'plain':
        print('format is plain')
    elif args.format == 'stylish':
        diff = generate_diff(args.first_file, args.second_file, stylish.format)
        print(diff)
    else:
        print('invalid format')
