#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for lst in matrix:
        for j in range(len(lst)):
            print("{:d}".format(lst[j]), end="")
            if j != len(lst) - 1:
                print(" ", end="")
        print("")
