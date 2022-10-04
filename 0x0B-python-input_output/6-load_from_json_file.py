#!/usr/bin/python3
"""This module contains function that creates
object from JSON file
"""

import json


def load_from_json_file(filename):
    """This function create object from JSON file"""

    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
