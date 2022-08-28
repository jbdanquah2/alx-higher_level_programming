#!/usr/bin/python3
def max_integer(my_list=[]):
    max = 0
    if not my_list:
        return None
    for el in my_list:
        if el > max:
            max = el
    return max
