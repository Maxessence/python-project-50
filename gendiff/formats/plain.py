#!/usr/bin/env python3


def convert(value):
    match value:
        case dict(value):
            return '[complex value]'
        case True | False:
            return str(value).lower()
        case None:
            return 'null'
        case int(value):
            return value
        case _:
            return (f"'{value}'")


def make_plain(difference: list) -> str:
    path = []

    def iter_(value, path):
        result = []
        for root in value:
            key = root.get('key')
            value = root.get('value')
            status = root.get('status')
            convert_value = convert(value)
            path.append(key)
            path_str = '.'.join(path)
            match status:
                case 'added':
                    result.append(f"Property '{path_str}' was added "
                                  f"with value: {convert_value}")
                case 'deleted':
                    result.append(f"Property '{path_str}' was removed")
                case 'changed':
                    old_value = convert(root.get('old'))
                    new_value = convert(root.get('new'))
                    result.append(f"Property '{path_str}' was updated. "
                                  f'From {old_value} to {new_value}')
                case 'children':
                    result.append(iter_(value, path))
            path.pop()
        return '\n'.join(result)

    return iter_(difference, path)
