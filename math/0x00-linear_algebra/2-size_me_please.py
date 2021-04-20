#!/usr/bin/env python3
""" Size Me Please """


def matrix_shape(matrix):
    """ calculates shape of a matrix """
    if matrix:
        shape = [len(matrix)]
        while type(matrix[0]) == list:
            shape.append(len(matrix[0]))
            matrix = matrix[0]
        return shape
    else:
        return [0]
