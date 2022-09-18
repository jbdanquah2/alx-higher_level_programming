#!/usr/bin/python3
"""
5-text_indentation
This module contains the text_indentation function

"""


def text_indentation(text):
    """This function prints out the text in a string
    each on a new line ending in ., ?, or :
    Args:
        param1: text - a string of text
    Returns: None
    Raises: TypeError
    """

    if not isinstance(text, str) or text is None:
        raise TypeError("text must be a string")

    txt = ""
    for ch in text.strip():
        if ch in [".", "?", ":"]:
            txt += ch
            print("{}".format(txt.strip()), end="")
            print("")
            print("")
            txt = ""
        else:
            txt += ch
    print("{}".format(txt.strip()), end="")
