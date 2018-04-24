#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from py_exercise.recursion import *


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)


def test_head():
    assert head([1, 2, 3]) == 1
    assert head([1]) == 1
    with pytest.raises(ValueError):
        head([])


def test_tail():
    assert tail([1, 2, 3]) == [2, 3]
    assert tail([1]) == []
    with pytest.raises(ValueError):
        tail([])
