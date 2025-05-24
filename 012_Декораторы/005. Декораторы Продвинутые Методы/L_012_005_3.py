#! python
# coding=utf-8
# **************************************************************
# L_012_005_3.py
# 012.Декораторы
# 005.Декораторы Продвинутые Методы
# --------------------------------------------------------------
# Практический Курс по Продвинутому Python (2023)
# https://www.udemy.com/course/avecoder-advanced-python/
# Ave Coder, 2023
# **************************************************************
# Writing by sgiman, May 2025

# ДЕКОРАТОРЫ, КОТОРЫЕ ВОЗВРАЩВАЮТ ДЕКОРАТОРЫ

# ОБЁРТКА (decorator)
def repeat(num):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(num):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return my_decorator


def greet(name):
    print(f"Hello, {name}")


#########################################################################
print('=' * 80)

# Выполнить 3 раза декоратор(обёртку) - repeat с функцией greet
greet_3_times = repeat(3)(greet)
greet_3_times("Alice")




