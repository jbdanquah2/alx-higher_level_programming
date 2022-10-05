#!/usr/bin/python3
"""Module 9-student"""


class Student:
    """This is the Student class"""

    def __init__(self, first_name, last_name, age):
        """This is the init method"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dict representation of Student"""

        return self.__dict__
