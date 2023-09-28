#!/usr/bin/env python3

import argparse


def get_arguments():
    parser = argparse.ArgumentParser(
        description='Generate difference between two files')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument(
        '-f', '--format',
        default='stylish',
        help='Set format of output. '
        'Option: stylish, plain, json (default stylish))')
    args = parser.parse_args()
    return args.first_file, args.second_file, args.format
