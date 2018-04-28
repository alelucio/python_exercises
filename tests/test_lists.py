#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from py_exercises.lists import *


@pytest.mark.parametrize("last_func,error_type", [
    (my_last, IndexError),
    (my_last_recursive, ValueError)
])
def test_my_last(last_func, error_type):
    assert last_func([1, 2, 3, 4]) == 4
    with pytest.raises(error_type):
        last_func([])


def test_my_last_recursive():
    assert my_last_recursive([1, 2, 3, 4]) == 4
    with pytest.raises(ValueError):
        my_last_recursive([])


def test_my_but_last():
    assert my_but_last([1, 2, 3, 4]) == 3
    with pytest.raises(IndexError):
        my_but_last([1])


def test_reverse_a_list():
    assert reverse_a_list(["c", "i", "a", "o"]) == ["o", "a", "i", "c"]
    assert reverse_a_list("ciao") == "oaic"
    assert reverse_a_list([]) == []
    assert reverse_a_list("ciao") != "miao"


def test_is_palindrome():
    assert is_palindrome("osso")
    assert not is_palindrome("pizza")
    assert is_palindrome([])


def test_destroy_duplicates():
    assert destroy_duplicates("babbbo") == "babo"
    assert destroy_duplicates("babbbo") != "babbo"


def test_destroy_duplicates_2():
    assert destroy_duplicates_2("babbbo") == "babo"
    assert destroy_duplicates_2("babbbo") != "babbo"


# aletzee test #

def test_select_number():
    assert select_number([1, 4, 5, 1, 3]) == [1, 1]
    assert select_number([]) == []
    assert select_number([1, 4, 5, 2, 3]) != [1, 1]


def test_select_number_1():
    assert select_number_1([1, 4, 5, 1, 3]) == [1, 1]
    assert select_number([]) == []
    assert select_number([1, 4, 5, 2, 3]) != [1, 1]


def test_sum_number():
    assert sum_number([1, 4, 5, 1, 3]) == 2
    # assert sum_number([]) == []#
    assert sum_number([1, 4, 5, 2, 3]) != 2


def test_three_of_kind_ones():
    assert three_of_kind_ones([1, 1, 1, 4, 5]) == 12
    assert three_of_kind_ones([1, 1, 1, 1, 6]) != 12
    # assert three_of_kind_ones([2, 2, 4, 5, 5]) != 12#


def test_three_of_kind_ones_1():
    assert three_of_kind_ones_1([1, 1, 1, 4, 5]) == 12
    assert three_of_kind_ones([1, 1, 4, 3, 6]) != 12


def test_four_of_kind_ones():
    assert four_of_kind_ones([1, 1, 1, 1, 6]) == 10
    assert four_of_kind_ones([1, 1, 5, 1, 6]) != 10


def test_large_straight():
    assert large_straight([1, 2, 3, 4, 5]) == 40
    assert large_straight([5, 2, 2, 4, 5]) != 40

