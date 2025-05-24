#! python
# coding=utf-8
# **************************************************************
# L_012_001.py
# 012.Декораторы
# 001.Знакомство с Декораторами
# --------------------------------------------------------------
# Практический Курс по Продвинутому Python (2023)
# https://www.udemy.com/course/avecoder-advanced-python/
# Ave Coder, 2023
# **************************************************************
# Writing by sgiman, May 2025


# Ф-Я ДЕКОРАТОР
def greet(func):
    def wrapper(*args, **kwargs):
        print('Hello')
        return func(*args, **kwargs)
    return wrapper

# Применить декоратор
@greet
def say_hello(name):
    print(f"Hello, {name}!")

##################################################################
print('=' * 80)
say_hello("John")
