#!/usr/bin/python3
"""This module contains fucntiotn to
append text to files
"""


def append_write(filename="", text=""):
    """This function append text to files"""

    with open(filename, 'a', encoding="utf-8") as f:
        num_characters = f.write(text)

    return num_characters
