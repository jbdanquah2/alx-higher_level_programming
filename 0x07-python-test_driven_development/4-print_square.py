#!/usr/bin/python3
"""
4-print_square module
This module contains print square module that prints
a sqaure with character #

"""


def print_square(size):
    """print a sqaure with a character #

    Args:
    param: size - the side length of the square

    Returns: None
    
    Raises: TypeError, ValueError
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
        return

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
