#!/usr/bin/env python3

from gendiff.formats.stylish import make_stylish
from gendiff.formats.json import make_json
from gendiff.formats.plain import make_plain
from gendiff.diff import diff


def make_formatting(old_data: dict, new_data: dict, format: str) -> list:
    difference = diff(old_data, new_data)
    match format:
        case 'stylish':
            return make_stylish(difference)
        case 'json':
            return make_json(difference)
        case 'plain':
            return make_plain(difference)
        case _:
            raise Exception('Unknown format')
