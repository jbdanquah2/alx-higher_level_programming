#!/usr/bin/python3
"""This is a module for Square class"""


class Square:
    """A class for Square type class"""

    def __init__(self, size=0, position=(0, 0)):
        """Init for the square class
        Args:
        param1: size is a private attribute of type int
        param2: positon is of type tuple for the position of the square
        """
        self.__size = size
        self.__position = position

    def area(self):
        """Returns the area of a square"""
        return (self.__size ** 2)

    def my_print(self):
        """Prints the square with #"""
        if self.__size == 0:
            print("")
            return

        [print("")for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(number, int) for number in value) or
                not all(number >= 0 for number in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
