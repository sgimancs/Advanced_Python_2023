#! python
# coding=utf-8
# **************************************************************
# L_012_001_4.py
# 012.Декораторы
# 001.Знакомство с Декораторами
# --------------------------------------------------------------
# Практический Курс по Продвинутому Python (2023)
# https://www.udemy.com/course/avecoder-advanced-python/
# Ave Coder, 2023
# **************************************************************
# Writing by sgiman, May 2025

# ----------------------
# НЕСКОЛЬКО ДЕКОРАТОРОВ
# ----------------------
# ДЕКОРАТОР
def decorator_1(func):
    def wrapper(*args, **kwargs):
        # Do something before
        print('John enters1 the room')
        result = func(*args, **kwargs)

        # Do something after
        return result

    return wrapper


def decorator_2(func):
    def wrapper(*args, **kwargs):
        # Do something before
        print('John enters2 the room')
        result = func(*args, **kwargs)
        print('John leaves the room')

        # Do something after
        return result

    return wrapper


# Применить декоратор
@decorator_1
@decorator_2
def greet(name):
    print("Hello, " + name)


################################################################
greet('John')
