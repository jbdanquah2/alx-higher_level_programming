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

        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")

        self.__width = width

    @property
    def height(self):
        """Height getter fucntion"""

        return self.__height

    @height.setter
    def height(self, height):
        """Height setter function"""

        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")

        self.__height = height

    @property
    def x(self):
        """x getter fucntion"""

        return self.__x

    @x.setter
    def x(self, x):
        """x setter function"""

        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")

        self.__x = x

    @property
    def y(self, y):
        """y getter function"""

        return y

    @y.setter
    def y(self, y):
        """y setter function"""

        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")

        self.__y = y

    def area(self):
        """Computes the area of the rectangle"""

        return (self.__width * self.__height)

    def display(self):
        """Draws the rectangle with #"""

        for i in range(self.__height):
            for j in range(self.__width):
                print("#", end="")
            print("")
