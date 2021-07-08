import argparse
from gendiff import gendiff


parser = argparse.ArgumentParser(description='Generate diff')

parser.add_argument('first_file', metavar='first_file', type=str)
parser.add_argument('second_file', metavar='second_file', type=str)
parser.add_argument(
    '-f', '--format',
    choices=('stylish', 'plain', 'json'),
    default='stylish',
    help='set format of output'
)

args = parser.parse_args()

if 'stylish' in args.format:
    print(gendiff(args.first_file, args.second_file, 'stylish'))
if 'plain' in args.format:
    print(gendiff(args.first_file, args.second_file, 'plain'))
if 'json' in args.format:
    print(gendiff(args.first_file, args.second_file, 'json'))
