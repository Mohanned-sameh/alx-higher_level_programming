#!/usr/bin/python3

"""
function: matrix_divided divides all the elements in a matrix
args: matrix, div
Return: a new matrix
"""


def matrix_divided(matrix, div):
    """
    matrix = [[i],[j]]
    """
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if type(matrix) != list or type(matrix[0]) != list or type(matrix[[0][0]]) != list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    return [[round(i / div, 2) for i in row] for row in matrix]
