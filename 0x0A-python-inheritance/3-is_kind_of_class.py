#!/usr/bin/python3
"""module checks the type of an object
"""


def is_kind_of_class(obj, a_class):
    """checks the type of obj
    Args:
        param1: obj
        param2: a_class
    Returns: True or False
    """
    if isinstance(obj, a_class):
        return (True)
    return (False)
