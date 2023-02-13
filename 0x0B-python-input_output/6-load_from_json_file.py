#!/usr/bin/python3
"""
A module that create obj
"""
from json import loads


def load_from_json_file(filename):
    """
    function that create obj
    """
    with open(filename, encoding='utf-8') as f:
        return loads(f.read())
