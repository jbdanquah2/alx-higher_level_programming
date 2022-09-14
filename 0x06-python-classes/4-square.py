#!/usr/bin/python3
"""This is a module for Square class"""


class Square:
    """A class for Square type class"""

    def __init__(self, size=0):
        """Init for the square class
        Args:
        param1: size is a private attribute of type int
        """
        self.size = size

    def area(self):
        """Returns the area of a square"""
        return (self.__size ** 2)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
