# -*- coding: utf-8 -*-
from py_exercises.recursion import *


def my_last(arr):
    """Find the last element of a list"""

    return arr[-1]


def my_last_recursive(arr):
    return head(arr) if not tail(arr) else my_last_recursive(tail(arr))


def my_but_last(arr):
    """Find the last but one element of a list"""

    return arr[-2]
