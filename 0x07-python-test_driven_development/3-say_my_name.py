#!/usr/bin/python3
"""
3-say_my_name module
This module has a function that prints first name and last name

"""
def say_my_name(first_name, last_name=""):
    """Prints a string with the first name and last name

    Args:
        first_name: first name of the user
        last_name: last name of the user

    Returns: a string - My name is <first name> <last name>
    """
    if (not isinstance(first_name, str) or
       first_name is None):
        raise TypeError("first_name must be a string")
    if (not isinstance(last_name, str) or last_name is None):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
