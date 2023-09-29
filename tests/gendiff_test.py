#!/usr/bin/env python3

import pytest
from gendiff.generated_diff import generate_diff
from gendiff.formats.formatter import make_formatting


file1_plain_json = "tests/fixtures/file1.json"
file2_plain_json = "tests/fixtures/file2.json"
file1_plain_yaml = "tests/fixtures/y_file1.yaml"
file2_plain_yaml = "tests/fixtures/y_file2.yaml"
file1_nested_json = "tests/fixtures/file1_nested.json"
file2_nested_json = "tests/fixtures/file2_nested.json"
file1_nested_yaml = "tests/fixtures/file1_nested.yaml"
file2_nested_yaml = "tests/fixtures/file2_nested.yaml"
plain_files = "tests/fixtures/plain_files.txt"
nested_result = "tests/fixtures/nested_result.txt"
plain_result = 'tests/fixtures/plain_result.txt'
json_result = 'tests/fixtures/json_result.txt'

datatest = [(file1_plain_json, file2_plain_json, plain_files),
            (file1_plain_yaml, file2_plain_yaml, plain_files),
            (file1_nested_json, file2_nested_json, nested_result),
            (file1_nested_yaml, file2_nested_yaml, nested_result)]

datatest2 = [(file1_nested_json, file2_nested_json, plain_result),
             (file1_nested_yaml, file2_nested_yaml, plain_result)]

datatest3 = [(file1_plain_json, file2_plain_json, json_result),
             (file1_plain_yaml, file2_plain_yaml, json_result)]


@pytest.mark.parametrize("file1, file2, result", datatest)
def test_stylish(file1, file2, result):
    diff = generate_diff(file1, file2)
    exp_result = make_formatting(diff, format='stylish')
    with open(result, "r") as f:
        text = f.read()
        assert exp_result == text


@pytest.mark.parametrize("file1, file2, result", datatest2)
def test_plain(file1, file2, result):
    diff = generate_diff(file1, file2)
    exp_result = make_formatting(diff, format="plain")
    with open(result, "r") as f:
        text = f.read()
        assert exp_result == text


@pytest.mark.parametrize("file1, file2, result", datatest3)
def test_json(file1, file2, result):
    diff = generate_diff(file1, file2)
    exp_result = make_formatting(diff, format="json")
    with open(result, "r") as f:
        text = f.read()
        assert exp_result == text
