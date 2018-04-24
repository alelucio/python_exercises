# -*- coding: utf-8 -*-


def fib(n):
    assert n > 0

    return fib(n - 1) + fib(n - 2) if n > 2 else 1


def head(arr):
    first, *_ = arr
    return first


def tail(arr):
    _, *rest = arr
    return rest
