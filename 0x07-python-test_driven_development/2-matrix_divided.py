#!/usr/bin/python3
"""
matrix_divided module
This module contains a function that divides all elements of a matrix

"""


def matrix_divided(matrix, div):
    """Divides the elements of a matrix

    Args:
    param1: matrix of type list
    param2: div of type int or float
    Returns: a new matrix

    Raise: TypeError, ZeroError
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if (not isinstance(matrix, list) or matrix == [] or
        not all(isinstance(lst, list) for lst in matrix) or
        not all((isinstance(ele, int) or isinstance(ele, float))
                for ele in [number for row in matrix for number in row])):
        raise TypeError("""matrix must be a matrix(list of lists)
                        of integers/floats""")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [list(map(lambda x: round(x / div, 2), row)) for row in matrix]
