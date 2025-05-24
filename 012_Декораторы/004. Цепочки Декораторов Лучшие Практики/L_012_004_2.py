#! python
# coding=utf-8
# **************************************************************
# L_012_004_2.py
# 012.Декораторы
# 004.Цепочки Декораторов Лучшие Практики
# --------------------------------------------------------------
# Практический Курс по Продвинутому Python (2023)
# https://www.udemy.com/course/avecoder-advanced-python/
# Ave Coder, 2023
# **************************************************************
# Writing by sgiman, May 2025


def decorator_1(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


def decorator_2(func):
    def wrapper(x, y, *args, **kwargs):
        return func(x, y, *args, **kwargs)
    return wrapper


@decorator_1        # 2 (signature 1)
@decorator_2        # 1 (signature 2)
def add(x, y):
    print(x + y)


################################################################
print('=' * 80)
add(5,5)


