#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_list = []
    for el in set_1:
        for ell in set_2:
            if el == ell:
                break
            new_list.append(el)
            new_list.append(ell)
    return new_list
