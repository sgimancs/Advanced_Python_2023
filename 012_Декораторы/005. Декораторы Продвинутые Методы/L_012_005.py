#! python
# coding=utf-8
# **************************************************************
# L_012_005.py
# 012.Декораторы
# 005.Декораторы Продвинутые Методы
# --------------------------------------------------------------
# Практический Курс по Продвинутому Python (2023)
# https://www.udemy.com/course/avecoder-advanced-python/
# Ave Coder, 2023
# **************************************************************
# Writing by sgiman, May 2025

# ОБЁРТКА (decorator)
def repeat(num):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(num):
                func(*args, **kwargs)
        return wrapper
    return my_decorator

# с вызовом декоратора 3 раза
@repeat(num=3)
def greet(name):
    print(f"Hello, {name}!")

greet("John")





