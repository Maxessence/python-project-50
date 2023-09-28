#!/usr/bin/env python3

from gendiff.formats.stylish import make_stylish
from gendiff.formats.json import make_json
from gendiff.generated_diff import generate_diff
from gendiff.parser import get_parse
from gendiff.formats.plain import make_plain


def make_formatting(first_file, second_file, format):
    old_data = get_parse(first_file)
    new_data = get_parse(second_file)
    difference = generate_diff(old_data, new_data)
    match format:
        case 'stylish':
            return make_stylish(difference)
        case 'json':
            return make_json(difference)
        case 'plain':
            return make_plain(difference)
