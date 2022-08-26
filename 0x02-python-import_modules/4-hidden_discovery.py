#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    lst = dir(hidden_4)
    for i in range(1, len(lst)):
        if lst[i][0] != "_":
            print("{:s}".format(lst[i]))
