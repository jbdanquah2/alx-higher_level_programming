#!/usr/bin/python3
"""This module contains the Square class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """This is the Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """This is the init function"""

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """str function"""

        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                  self.y, self.width))
    @property
    def size(self):
        """getter fucntion for size"""

        return self.width

    @size.setter
    def size(self, value):
        """setter function for size"""

        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value
        self.__height = value
