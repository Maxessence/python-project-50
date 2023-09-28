#!/usr/bin/env python3


def generate_diff(old_data: dict, new_data: dict) -> list:
    keys = old_data.keys() | new_data.keys()
    result = []
    for k in sorted(keys):
        old_value = old_data.get(k)
        new_value = new_data.get(k)
        if k not in new_data:
            result.append({'key': k, 'status': 'deleted',
                           'value': old_data[k]})
        elif k not in old_data:
            result.append({'key': k, 'status': 'added',
                           'value': new_data[k]})
        elif isinstance(old_data[k], dict) and isinstance(new_data[k], dict):
            result.append({'key': k, 'status': 'children',
                           'value': generate_diff(old_value, new_value)})
        elif old_data[k] == new_data[k]:
            result.append({
                'key': k, 'status': 'unchanged', 'value': old_value})
        else:
            result.append({'key': k, 'status': 'changed',
                           'old': old_value, 'new': new_value})
    return result
