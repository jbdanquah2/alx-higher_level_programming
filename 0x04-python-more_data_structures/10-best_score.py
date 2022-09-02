#!/usr/bin/python3
def best_score(a_dictionary):
    if isinstance(a_dictionary, dict):
        key = None
        m = 0
        for k, v in a_dictionary.items():
            if v > m:
                key = k
                m = v
        return key
