#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    length = len(argv)
    arg = "arguments:" if length - 1 > 1 else "argument."
    print("{:d} {:s}".format(length - 1, arg))
    if length > 1:
        for i in range(1, length):
            print("{:d}: {:s}".format(i, argv[i]))
