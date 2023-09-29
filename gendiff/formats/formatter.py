#!/usr/bin/env python3

from gendiff.formats.stylish import make_stylish
from gendiff.formats.json import make_json
from gendiff.formats.plain import make_plain


def make_formatting(difference, format):
    match format:
        case 'stylish':
            return make_stylish(difference)
        case 'json':
            return make_json(difference)
        case 'plain':
            return make_plain(difference)
        case _:
            raise Exception('Unknown format')
