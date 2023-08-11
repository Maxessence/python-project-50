#!/usr/bin/env python3


from gendiff.tree import generate_diff


file1 = "/home/maxis/Documents/python-project-50/tests/file1.json"
file2 = "/home/maxis/Documents/python-project-50/tests/file2.json"
result_json = "/home/maxis/Documents/python-project-50/tests/result_json.json"


def test_json():
        with open(result_json, 'r') as f:
                exp_result = f.read()
        assert generate_diff(file1, file2) == exp_result
        


