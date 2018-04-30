# -*- coding: utf-8 -*-
from functools import reduce

from py_exercises.recursion import *


def my_last(arr):
    """Find the last element of a list"""

    return arr[-1]


def my_last_recursive(arr):
    return head(arr) if not tail(arr) else my_last_recursive(tail(arr))


def my_but_last(arr):
    """Find the last but one element of a list"""

    return arr[-2]


# inverti una lista #

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


# funzioni aletzee #

def select_number(arr):
    return list(filter(lambda x: x == 1, arr))


def select_number_1(arr):
    lista_numeri = list(filter(lambda x: x == 1, arr))
    return lista_numeri
    print(lista_numeri)


def sum_number(arr):
    return reduce(lambda x, y: x + y, select_number(arr))  # fatto ma non capito benissimo#


def three_of_kind_ones(arr):
    if sum_number(arr) == 3:
        return sum(arr)
    else:
        return None


def three_of_kind_ones_1(arr):
    return sum(arr) if sum_number(arr) == 3 else None


def four_of_kind_ones(arr):
    return sum(arr) if sum_number(arr) == 4 else None


def large_straight(arr):
    arr.sort()
    if sum(arr) == 15 or sum(arr) == 20:
        return 40
    else:
        return None


def aletzee(arr):
    if len(set(arr)) == 1:
        return 50
    else:
        return None


def full_house(arr):
    arr.sort()
    if len(set(arr)) == 2 and sum(arr[0:2]) == arr[0] * 2 and sum(arr[2:5]) == arr[2] * 3 or len(set(arr)) == 2 and sum(
            arr[0:3]) == arr[0] * 3 and sum(arr[3:5]) == arr[3] * 2:
        return 25
    else:
        return None


def destroy_duplycates_3(arr):
    result = list(set(arr))
    return result[0:4]


def small_straight(arr):
    if sum(destroy_duplycates_3(arr)) == 10 or sum(destroy_duplycates_3(arr)) == 14 or sum(destroy_duplycates_3(arr)) == 18:
        return 30
    else:
        return None
