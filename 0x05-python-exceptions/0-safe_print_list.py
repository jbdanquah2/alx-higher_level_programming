#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if isinstance(my_list, list) and x != 0:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
        return (x)