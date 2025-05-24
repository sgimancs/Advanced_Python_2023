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

import logging

# decorator
def handle_errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.error(f"Error occurred in {func.__name__}: {e}")
    return wrapper

@handle_errors
def divide(x, y):
    return x / y


#####################################################################
print('=' * 80)
print(divide(1, 0))



