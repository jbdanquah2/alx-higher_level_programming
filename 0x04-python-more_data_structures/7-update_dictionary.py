#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    new_dict = {}
    if isinstance(a_dictionary, dict):
        for k, v in a_dictionary.items():
            if k == key:
                v = value
            new_dict[k] = v
    return new_dict
