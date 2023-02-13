#!/usr/bin/python3
"""
A module that print json rep
"""
from json import dumps


def to_json_string(my_obj):
    """
    function that print json representation
    """
    return dumps(my_obj)
