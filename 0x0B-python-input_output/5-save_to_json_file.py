#!/usr/bin/python3
"""This module contains function that writes object
to a file using JSON
"""

import json


def save_to_json_file(my_obj, filename):
    """This function writes object to text file using JSON"""

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
