#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if isinstance(my_list, list) and x != 0:
        try:
            for i in range(x):
                print("{}".format(my_list[i]), end="")
        except IndexError:
            x = i
        print("")

        return (x)
