#!/usr/bin/python3
import sys
l = len(sys.argv)
arg = "arguments" if l - 1 > 1 else "argument"
print("{} {}".format(l - 1, arg))
if l > 1:
    for i in range(1, l):
        print("{}: {}".format(i, sys.argv[i]))
