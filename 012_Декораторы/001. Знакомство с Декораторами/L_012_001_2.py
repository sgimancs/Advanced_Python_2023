#! python
# coding=utf-8
# **************************************************************
# L_012_001_2.py
# 012.Декораторы
# 001.Знакомство с Декораторами
# --------------------------------------------------------------
# Практический Курс по Продвинутому Python (2023)
# https://www.udemy.com/course/avecoder-advanced-python/
# Ave Coder, 2023
# **************************************************************
# Writing by sgiman, May 2025

# ДЕКОРАТОР
def log_function(func):
    def wrapper(*args, **kwargs):
        print(f"Log: {func.__name__} was called")
        return func(*args, **kwargs)
    return wrapper


# Применить декоратор
@log_function
def add(x, y):
    return x + y

#################################################################
print('=' * 80)
add(5, 2)


