#!/usr/bin/python3
"""
A module that appends to a file
"""


def append_write(filename="", text=""):
    """
    A function that appends
    """
    with open(filename, mode='a', encoding='utf-8') as f:
        return f.write(text)
