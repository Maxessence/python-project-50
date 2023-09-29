#!/usr/bin/env python3

from gendiff.parser import get_parse
from gendiff.diff import diff
from gendiff.formats.formatter import make_formatting


def generate_diff(first_file, second_file, format):
    old_data = get_parse(first_file)
    new_data = get_parse(second_file)
    difference = diff(old_data, new_data)
    result = make_formatting(difference, format)
    return result
