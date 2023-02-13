#!/usr/bin/python3
"""
A module that opens and read a file
"""


def read_file(filename=""):
    """
    a function that opens and prints a file
    """
    with open(filename, encoding='utf-8') as f:
        for line in f:
            print(line, end='')
