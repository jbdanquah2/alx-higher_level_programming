#!/usr/bin/python3
"""This module contains the Rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """This is the Rectangle class with all the
    fucntions required. It inherits the Base class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Width get function"""

        return self.__width

    @width.setter
    def width(self, width):
        """Width setter function"""

        self.__width = width

    @property
    def height(self):
        """Height getter fucntion"""

        return self.__height

    @height.setter
    def height(self, height):
        """Height setter function"""

        self.__height = height

    @property
    def x(self):
        """x getter fucntion"""

        return self.__x

    @x.setter
    def x(self, x):
        """x setter function"""

        self.__x = x

    @property
    def y(self, y):
        """y getter function"""

        return y

    @y.setter
    def y(self, y):
        """y setter function"""

        self.__y = y
