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


def test_pack():
    assert pack(['a', 'a', 'a', 'b', 'b', 'd', 'e', 'd', 'e']) == ['aaa', 'bb', 'dd', 'ee']


def test_encode():
    assert encode(['a', 'a', 'a', 'b', 'b', 'd', 'e', 'd', 'e']) == [(3, 'a'), (2, 'b'), (2, 'd'), (2, 'e')]


def test_question_11():
    assert question_11(['a', 'a', 'a', 'a', 'b', 'c', 'c', 'a', 'a', 'd', 'e', 'e', 'e', 'e']) == [(4, 'a'), 'b',
                                                                                                   (2, 'c'), (2, 'a'),
                                                                                                   'd', (4, 'e')]


def test_question_14mio():
    assert question_14mio(['a', 'b', 'c', 'c', 'd']) == ['a', 'a', 'b', 'b', 'c', 'c', 'c', 'c', 'd', 'd']


def test_question_14():
    assert question_14(['a', 'b', 'c', 'c', 'd']) == ['a', 'a', 'b', 'b', 'c', 'c', 'c', 'c', 'd', 'd']