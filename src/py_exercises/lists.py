# -*- coding: utf-8 -*-
from functools import reduce
from itertools import groupby
from py_exercises.recursion import *


def my_last(arr):
    """Find the last element of a list"""

    return arr[-1]


def my_last_recursive(arr):
    return head(arr) if not tail(arr) else my_last_recursive(tail(arr))


def my_but_last(arr):
    """Find the last but one element of a list"""

    return arr[-2]


def reverse_a_list(arr):
    return arr[::-1]


# palindromo o no#

def is_palindrome(arr):
    if arr[::1] == arr[::-1]:
        return True
    else:
        return False


def is_palindrome_1(arr):
    return arr[::1] == arr[::-1]


def is_palindrome_2(arr):
    return arr == reverse_a_list(arr)


# togli i duplicati #

def destroy_duplicates(arr):
    def compatta(acc, nextt):
        if nextt == acc[-1]:
            return acc
        else:
            return acc + nextt

    return reduce(compatta, arr)


def destroy_duplicates_1(arr):
    def compatta(acc, nextt):
        return acc if nextt == acc[-1] else acc + nextt

    return reduce(compatta, arr)


def destroy_duplicates_2(arr):
    return reduce(lambda acc, nextt: acc if nextt == acc[-1] else acc + nextt, arr)


# impacca di duplicati di una lista di elementi in una sottolista

def pack(arr):
    arr.sort()

    def pippo(acc, nextt):
        if nextt == acc[-1]:
            return acc + nextt

        else:
            return acc + " " + nextt

    return reduce(pippo, arr).split(" ")


def encode(arr):
    arr.sort()
    return [(len(list(group)), key) for key, group in groupby(arr)]
