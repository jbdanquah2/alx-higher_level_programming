#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if isinstance(matrix, list):
        return [list(map(lambda x: x ** 2, row)) for row in matrix]
