#!/usr/bin/python3
"""This module contains a class the inherits
from a list obj.
"""


class MyList(list):
    """This class inherits from a list obj
    """

    def print_sorted(self):
        """Prints the elements of a list in ascending order
        """
        print("{}".format(sorted(self)))
