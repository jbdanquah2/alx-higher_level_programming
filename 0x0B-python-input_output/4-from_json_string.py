#!/usr/bin/python3
"""This module contains function that
return python object from json string
"""

import json


def from_json_string(my_str):
    """This function returns python object from
    json string
    """

    return json.loads(my_str)
