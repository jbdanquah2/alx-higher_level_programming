#!/usr/bin/python3
def uniq_add(my_list=[]):
    if isinstance(my_list):
        sum = 0
        new_list = list(set(my_list))
        for el in new_list:
            sum += el
        return sum
