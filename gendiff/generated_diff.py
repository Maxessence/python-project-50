#!/usr/bin/env python3

from gendiff.parser import get_parse
from gendiff.diff import diff


def generate_diff(first_file: str, second_file: str) -> list:
    old_data = get_parse(first_file)
    new_data = get_parse(second_file)
    difference = diff(old_data, new_data)
    return difference
