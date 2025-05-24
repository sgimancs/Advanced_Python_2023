#! python
# coding=utf-8
# **************************************************************
# L_012_004.py
# 012.Декораторы
# 004.Цепочки Декораторов Лучшие Практики
# --------------------------------------------------------------
# Практический Курс по Продвинутому Python (2023)
# https://www.udemy.com/course/avecoder-advanced-python/
# Ave Coder, 2023
# **************************************************************
# Writing by sgiman, May 2025

from inspect import signature


def decorator_1(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    wrapper.__signature__ = signature(func)
    wrapper.__doc__ = func.__doc__
    return wrapper


@decorator_1
def add(x: int, y: int) -> int:
    """Returns the sum of x and y."""
    print(x + y)


################################################################
print('=' * 80)
add(5,2)


