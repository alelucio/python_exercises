#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from py_exercise.lists import *


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
