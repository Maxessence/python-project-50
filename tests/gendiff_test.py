#!/usr/bin/env python3

import pytest
from gendiff.formats.formatter import make_formatting


file1_plain_json = "tests/fixtures/file1.json"
file2_plain_json = "tests/fixtures/file2.json"
file1_plain_yaml = "tests/fixtures/y_file1.yaml"
file2_plain_yaml = "tests/fixtures/y_file2.yaml"
file1_nested_json = "tests/fixtures/file1_nested.json"
file2_nested_json = "tests/fixtures/file2_nested.json"
file1_nested_yaml = "tests/fixtures/file1_nested.yaml"
file2_nested_yaml = "tests/fixtures/file2_nested.yaml"
flat_result = "tests/fixtures/plain_result.txt"
nested_result = "tests/fixtures/nested_result.txt"
datatest = [(file1_plain_json, file2_plain_json, flat_result),
            (file1_plain_yaml, file2_plain_yaml, flat_result),
            (file1_nested_json, file2_nested_json, nested_result),
            (file1_nested_yaml, file2_nested_yaml, nested_result)]


@pytest.mark.parametrize("file1, file2, result", datatest)
def test_json(file1, file2, result):
    exp_result = make_formatting(file1, file2, format="stylish")
    with open(result, "r") as f:
        text = f.read()
        assert exp_result == text
