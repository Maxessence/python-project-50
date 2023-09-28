#!/usr/bin/env python3

import itertools


Added = "+ "
Deleted = "- "
Indent = "  "


def unpack(value, depth, replacer):
    result = []
    spaces_count = 4
    deep_indent_size = depth * spaces_count - 2
    deep_indent = replacer * deep_indent_size
    current_indent = replacer * (deep_indent_size - 2)
    nested = depth + 1
    if isinstance(value, dict):
        for key, value in value.items():
            result.append(f'{deep_indent}{Indent}{key}: '
                          f'{unpack(value, nested, replacer)}')
        result = itertools.chain("{", result, [current_indent + "}"])
        return '\n'.join(result)
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    else:
        return value


def make_stylish(tree, replacer=' ', spaces_count=4):

    def iter_(current_value, depth):
        deep_indent_size = depth * spaces_count - 2
        deep_indent = replacer * deep_indent_size
        current_indent = replacer * (deep_indent_size - 2)
        lines = []
        nested = depth + 1
        for root in current_value:
            key = root.get('key')
            value = root.get('value')
            status = root.get('status')
            unpack_value = unpack(value, nested, replacer)
            match status:
                case 'added':
                    lines.append(f'{deep_indent}{Added}{key}: {unpack_value}')
                case 'deleted':
                    lines.append(f'{deep_indent}{Deleted}{key}: '
                                 f'{unpack_value}')
                case 'unchanged':
                    lines.append(f'{deep_indent}{Indent}{key}: {unpack_value}')
                case 'changed':
                    old_value = unpack(root.get('old'), nested, replacer)
                    new_value = unpack(root.get('new'), nested, replacer)
                    lines.append(f'{deep_indent}{Deleted}{key}: {old_value}')
                    lines.append(f'{deep_indent}{Added}{key}: {new_value}')
                case 'children':
                    lines.append(f'{deep_indent}{Indent}{key}: '
                                 f'{iter_(value, nested)}')
            result = itertools.chain('{', lines, [current_indent + '}'])
        return '\n'.join(result)

    return iter_(tree, 1)
