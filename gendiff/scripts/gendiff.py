#!/usr/bin/env python3


from gendiff.cli import get_arguments
from gendiff.generated_diff import generate_diff
from gendiff.formats.formatter import make_formatting


def main():
    first_file, second_file, format = get_arguments()
    diff = generate_diff(first_file, second_file)
    result = make_formatting(diff, format)
    print(result)


if __name__ == '__main__':
    main()
