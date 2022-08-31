#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    s1 = list(set_1 - set_2)
    s2 = list(set_2 - set_1)
    return s1 + s2
