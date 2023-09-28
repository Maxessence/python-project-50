#!/usr/bin/env python3


from gendiff.cli import get_arguments
from gendiff.formats.formatter import make_formatting


def main():
    first_file, second_file, format = get_arguments()
    result = make_formatting(first_file, second_file, format)
    print(result)


if __name__ == '__main__':
    main()
