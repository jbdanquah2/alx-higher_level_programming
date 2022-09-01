#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if isinstance(a_dictionary, dict):
        new_dict = {}
        for k, v in a_dictionary.items():
            new_dict[k] = v
        new_dict[key] = value
    return new_dict
