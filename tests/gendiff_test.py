#!/usr/bin/env python3

import pytest
from gendiff.tree import generate_diff
from gendiff.parser import get_parse
import json


file1_flat_json = "tests/fixtures/file1.json"
file2_flat_json = "tests/fixtures/file2.json"
file1_flat_yaml = "tests/fixtures/y_file1.yaml"
file2_flat_yaml = "tests/fixtures/y_file2.yaml"
flat_result = "tests/fixtures/result_json.json"


@pytest.mark.parametrize("file1", [file1_flat_json, file1_flat_yaml])
@pytest.mark.parametrize("file2", [file2_flat_json, file2_flat_yaml])
@pytest.mark.parametrize("result", [flat_result, flat_result])
def test_json(file1, file2, result):
    data = get_parse(result)
    exp_result = json.dumps(data, indent=4)
    assert generate_diff(file1, file2) == exp_result
