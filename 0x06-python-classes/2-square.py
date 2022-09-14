#!/usr/bin/python3
"""This is a module for Square class"""


class Square:
    """A class for Square type class"""

    def __init__(self, size=0):
        """Init for the square class
        Args:
        param1: size is a private attribute of type int
        """
        if not isinstance(size, int):
            raise ValueError("size must be an integer")
        elif size < 0:
            raise TypeError("size must be >= 0")

        self.__size = size
