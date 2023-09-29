#!/usr/bin/env python3


from gendiff.cli import get_arguments
from gendiff.generated_diff import generate_diff


def main():
    first_file, second_file, format = get_arguments()
    result = generate_diff(first_file, second_file, format)
    print(result)


if __name__ == '__main__':
    main()
