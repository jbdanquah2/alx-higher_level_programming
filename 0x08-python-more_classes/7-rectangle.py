#!/usr/bin/python3
"""This module contains a class
that defines a rectangle
"""


class Rectangle:
    """Defines a rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Init for the Rectangle class
        Args:
        param1: this is the width of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2 * (self.__width + self.__height))

    def __str__(self):
        if not (self.__width == 0 or self.__height == 0):

            for i in range(self.__height):
                for j in range(self.__width):
                    print(Rectangle.print_symbol, end="")
                if i != self.__height - 1:
                    print("")
        return ""

    def __repr__(self):
        return "Rectangle("+str(self.__width)+", "+str(self.__height)+")"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
