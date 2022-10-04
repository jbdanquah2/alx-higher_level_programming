#!/usr/bin/python3
"""This module contains function to convert
objects to JSON
"""

import json


def to_json_string(my_obj):
    """This fucntion returns the JSON representation
    of objects
    """

    return json.dumps(my_obj)
