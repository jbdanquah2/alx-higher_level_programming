#!/usr/bin/python3
"""This is a module for Square class"""


class Square:
    """A class for Square type class"""

    def __init__(self, size=0):
        """Init for the square class
        Args:
        param1: size is a private attribute of type int
        """
        self.__size = size

    def area(self):
        """Returns the area of a square"""
        return (self.__size ** 2)

    def my_print(self):
        """Prints the square with #"""
        if self.__size == 0:
            print("")
            return
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print("")

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
