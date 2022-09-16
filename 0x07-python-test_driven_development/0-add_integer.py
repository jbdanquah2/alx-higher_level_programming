#!/usr/bin/python3
"""
add_integermodule
This module contains function for adding integers

"""


def add_integer(a, b=98):
    """Computes or add two integers
    Returns: int: a + b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
