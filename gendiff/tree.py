#!/usr/bin/env python3

import json
from gendiff.parser import get_parse


def generate_diff(file1, file2):
    data1 = get_parse(file1)
    data2 = get_parse(file2)
    diff_dict = {}
    for key1 in sorted(data1):
        if key1 in data2:
            if data1[key1] == data2[key1]:
                diff_dict["  " + key1] = data1[key1]
            else:
                diff_dict["- " + key1] = data1[key1]
                diff_dict["+ " + key1] = data2[key1]
        else:
            diff_dict["- " + key1] = data1[key1]
    for key2 in sorted(data2):
        if key2 not in data1:
            diff_dict["+ " + key2] = data2[key2]
    result = json.dumps(diff_dict, indent=4)
    return result
