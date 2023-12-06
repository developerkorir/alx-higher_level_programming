#!/usr/bin/python3

from functools import reduce


def uniq_add(my_list=[]):
    unique_list = set(my_list)
    return reduce((lambda x, y:x + y), unique_list)
