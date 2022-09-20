#!/usr/bin/python3
"""This module implements a LockedClass
"""


class LockedClass:
    """This class only allows first_name attribute to be created
    """

    __slots__ = ["first_name"]
