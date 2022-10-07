#!/usr/bin/python3
"""Module 11-student"""


class Student:
    """This is the Student class"""

    def __init__(self, first_name, last_name, age):
        """This is the init method"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dict representation of Student"""

        if (isinstance(attrs, list) and all(type(elem) == str
                                            for elem in attrs)):
            return {attr: getattr(self, attr) for attr in attrs
                    if hasattr(self, attr)}
        return self.__dict__

    def reload_from_json(self, json):
        """Set instance attributes from JSON"""

        for name, value in json.items():
            settr(self, name, value)
