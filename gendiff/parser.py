#!/usr/bin/env python3

import yaml
import json
import os


def get_open(file):
    data = open(file)
    return data


def get_format(file):
    split_up = os.path.splitext(file)
    file_extenthion = split_up[1]
    return file_extenthion


def get_parse(file):
    data = get_open(file)
    format = get_format(file)
    match format:
        case ".json":
            data = json.load(data)
            return data
        case ".yaml":
            data = yaml.load(data, Loader=yaml.Loader)
            return data
        case ".yml":
            data = yaml.load(data, Loader=yaml.Loader)
            return data
