#!/usr/bin/env python3
""" Howdy Partner """


def cat_arrays(arr1, arr2):
    """ Concatenates two arrays """

    new_list = list(arr1)
    for i in range(len(arr2)):
        new_list.append(arr2[i])
    return new_list
