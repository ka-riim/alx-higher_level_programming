#!/usr/bin/python3
"""
A module that returns obj
"""
from json import loads


def from_json_string(my_str):
    """
    function that return obj
    """
    return loads(my_str)
