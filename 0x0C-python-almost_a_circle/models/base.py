#!/usr/bin/python3
"""This module contains the base class
for this project
"""


class Base:
    """This is the base class of the project
    """

    __nb_objects = 0

    def __init__(self, id=None):
        self.id = id

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        if id is not None:
            self.__id = id
        else:
            Base.__nb_objects += 1
            self.__id = Base.__nb_objects
