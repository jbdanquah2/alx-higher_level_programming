#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if isinstance(a_dictionary, dict):
        new_dict = {}
        for k, v in a_dictionary.items():
            new_dict[k] = v
        del new_dict[k]
    return new_dict
