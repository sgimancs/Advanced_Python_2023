#! python
# coding=utf-8
# **************************************************************
# L_012_005_2.py
# 012.Декораторы
# 005.Декораторы Продвинутые Методы
# --------------------------------------------------------------
# Практический Курс по Продвинутому Python (2023)
# https://www.udemy.com/course/avecoder-advanced-python/
# Ave Coder, 2023
# **************************************************************
# Writing by sgiman, May 2025

# ОБЁРТКА (decorator)
def repeat(num, *, after=None, before=None):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            if before is not None:
                before()
            for i in range(num):
                func(*args, **kwargs)
            if after is not None:
                after()
        return wrapper
    return my_decorator


def before_greeting():
    print("I'm doing something before the decoration function is called.")


def after_greeting():
    print("I'm doing something after the decoration function is called.")


@repeat(num=2, before=before_greeting, after=after_greeting)
def greet(name):
    print(f"Hello, {name}!")


#########################################################################
print('=' * 80)
greet("John")






