#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    length = len(argv)
    arg = "arguments" if (length - 1 > 1) or (length - 1 == 0) else "argument"
    punc = ":" if (length - 1) >= 1 else "."
    print("{:d} {:s}{:s}".format((length - 1), arg, punc))
    if length > 1:
        for i in range(1, length):
            print("{:d}: {:s}".format(i, argv[i]))

