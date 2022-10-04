#!/usr/bin/python3
"""This module contains function that read
text files
"""


def read_file(filename=""):
    """This function reads text file"""

    with open(filename, 'r') as f:
        for line in f:
            print(line, end="")
