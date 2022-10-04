#!/usr/bin/python3
"""This module contains functoin to
to write a string to a file
"""


def write_file(filename="", text=""):
    """This function writes a text string to file"""

    with open(filename, "w", encoding="utf-8") as f:
        num_characters = f.write(text)

    return num_characters
