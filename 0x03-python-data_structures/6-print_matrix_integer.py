#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        s = " "
        for j in range(len(i)):
            if j == len(i) - 1:
                s = ""
            print("{:d}".format(j), end=s)
        print("\r")
