#!/usr/bin/env python3
"""Flip Me Over"""


def matrix_transpose(matrix):
    """transpose a matrix"""

    new_matrix = []
    for i in range(len(matrix[0])):
        new_row = []
        for j in range(len(matrix)):
            new_row.append(matrix[j][i])
        new_matrix.append(new_row)
    return new_matrix
