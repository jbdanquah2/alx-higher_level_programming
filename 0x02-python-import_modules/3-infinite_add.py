#!/usr/bin/python3
import sys
length = len(sys.argv)
sum = 0
if length > 1:
    for i in range(1, length):
        sum += int(sys.argv[i])
print("{}".format(sum))
