#!/usr/bin/python3
"""This module contains the Square class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """This is the Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """This is the init function.
        It inherits the Rectangle class
        """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """str function"""

        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                  self.y, self.width))

    @property
    def size(self):
        """getter fucntion for size"""

        return self.size

    @size.setter
    def size(self, value):
        """setter function for size"""

        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        """update function"""

        if args and len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
                i += 1

        elif kwargs and len(kwargs) != 0:
            for j, k in kwargs.items():
                if j == "id":
                    if k is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = k
                elif j == "size":
                    self.size = k
                elif j == "x":
                    self.x = k
                elif j == "y":
                    self.y = k

    def __str__(self):
        """__str__ function"""

        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    def to_dictionary(self):
        """to_dictionary function"""

        return {
            "id": self.id, "size": self.width, "x": self.x, "y": self.y
        }
