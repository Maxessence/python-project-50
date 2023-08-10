#!/usr/bin/env python3


import json


def get_open(file1, file2):
    data1 = json.load(open(file1))
    data2 = json.load(open(file2))
    return data1, data2


# def get_values(data1 , data2, key):
#   value1 = data1.get(key)
#   value2 = data2.get(key)
#   if value1 is None:
#     key = f"+ {key}"
#     return key, value2
#   if value1 is not None and value2 is None:
#     key = f"- {key}"
#     return key, value1
#   if value1 == value2:
#     return "unchanged"
#   if value1 != value2:
#     return "changed"


# file1 = "gendiff/tests/file1.json"
# file2 = "gendiff/tests/file2.json"


def generate_diff(file1, file2):
    data1, data2 = get_open(file1, file2)
    diff_dict = {}
    # set_of_keys = data1.keys() | data2.keys()
    # for key in set_of_keys:
    #   diff_dict[key] = get_values(data1 , data2, key)
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

# print(generate_diff(file1,file2))
