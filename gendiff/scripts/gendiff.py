import argparse
from gendiff import generate_diff


def main():
    parser = argparse.ArgumentParser(
                    prog='gendiff',
                    description='Compares two configuration files \
                        and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', type=str,
                        help='set format of output')
    args = parser.parse_args()
    if args.format == 'plain':
        print('format is plain')
    elif args.format == 'json':
        diff = generate_diff(args.first_file, args.second_file)
        print(diff)
    else:
        print('invalid format')
