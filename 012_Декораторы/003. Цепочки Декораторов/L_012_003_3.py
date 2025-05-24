#! python
# coding=utf-8
# **************************************************************
# L_012_003_2.py
# 012.Декораторы
# 003.Цепочки Декораторов
# --------------------------------------------------------------
# Практический Курс по Продвинутому Python (2023)
# https://www.udemy.com/course/avecoder-advanced-python/
# Ave Coder, 2023
# **************************************************************
# Writing by sgiman, May 2025

# decorator 1
def bold(func):
    def wrapper(*args, **kwargs):
        return f"<b>{func(*args, **kwargs)}</b>"
    return wrapper


# decorator 2
def itallic(func):
    def wrapper(*args, **kwargs):
        return f"<i>{func(*args, **kwargs)}</i>"
    return wrapper


@bold                           # 2
@itallic                        # 1
def greet(name):
    return f"Hello, {name}"


#####################################################################
print('=' * 80)
print(greet("Alice"))



