#!/usr/bin/python3
for i in range(0, 100):
    s = " " if i == 99 else ", "
    print("{:02d}".format(i), end=s)
print("\n")
