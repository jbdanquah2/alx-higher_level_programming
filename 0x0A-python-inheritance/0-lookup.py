#!/usr/bin/python3
"""This module contains a function to check
list of available attributes and methods on an object
"""


def lookup(obj):
    """Returns a list of available atributes and methods of obj
    Args:
        param1: object
    Returns: list
    """

    lst = dir(obj)
    return (lst)
