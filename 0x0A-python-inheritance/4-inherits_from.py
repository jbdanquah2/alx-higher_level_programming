#!/usr/bin/python3
"""checks the instance of an object
"""


def inherits_from(obj, a_class):
    """checks the instance of a specified object
    Args:
        param1: obj
        param2: a_class
    Returns: True or False
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return (True)
    return (False)
