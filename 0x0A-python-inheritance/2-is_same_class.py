#!/usr/bin/python3
"""checks if that an object is the instance of class
"""


def is_same_class(obj, a_class):
    """This functions checks if obj is instance of a_class
    Args:
        param1: obj
        param2: a_classs
    Returns: True or False
    """
    if not isinstance(obj, a_class):
        return (False)

    return (True)
