#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    if isinstance(my_list, list) and x != 0:
        try:
            for i in range(x):
                print("{:d}".format(), end="")
        except ValueError:
            i = i - 1
        except IndexError:
            x = i

        return (x)
            