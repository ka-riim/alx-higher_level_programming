#!/usr/bin/python3
"""
A module that save to json
"""
from json import dumps


def save_to_json_file(my_obj, filename):
    """
    function that saves to json
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        f.write(dumps(my_obj))
