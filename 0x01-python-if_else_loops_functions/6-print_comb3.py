#!/usr/bin/python3
# loop through the number: firt loop
# loop through the numbers again: second loop
# pair the numbers after checking the pair are not the same
# compare and print the smallest of the pairs
# print numbers in ascending order

for i in range(10):
    for j in range(10):
        if i != j and i < j:
            n = f"{i}{j}"
            m = f"{j}{i}"
            z = n if n < m else m
            print("{}".format(z), end=", " if int(z) < 89 else None)
        else:
            pass
