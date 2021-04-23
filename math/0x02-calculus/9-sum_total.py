#!/usr/bin/env python3
""" calculates summation """


def summation_i_squared(n):
    """ making a summation function """
    if type(n) is not int or n < 1:
        return None
    if n == 1:
        return 1
    else:
        return int((n*((n+1)*(2*n+1))) / 6)
