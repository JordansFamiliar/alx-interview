#!/usr/bin/python3
"""A function that returns a list of lists of
   integers representing Pascal's triangle of n
"""


def pascal_triangle(n):
    """
    Returns a list of integers
    representing the Pascal Triangle of n
    returns empty list if n <= 0
    """
    matrix = []

    if n <= 0:
        return matrix

    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                value = matrix[i - 1][j - 1] + matrix[i - 1][j]
                row.append(value)
        matrix.append(row)

    return matrix
