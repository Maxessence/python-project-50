#!/usr/bin/env python3

from gendiff.parser import get_parse
from gendiff.formats.formatter import make_formatting


def generate_diff(first_file: str, second_file: str, format="stylish") -> list:
    old_data = get_parse(first_file)
    new_data = get_parse(second_file)
    result = make_formatting(old_data, new_data, format)
    return result
