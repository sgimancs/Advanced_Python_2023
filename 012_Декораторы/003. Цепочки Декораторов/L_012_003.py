#! python
# coding=utf-8
# **************************************************************
# L_012_003.py
# 012.Декораторы
# 003.Цепочки Декораторов
# --------------------------------------------------------------
# Практический Курс по Продвинутому Python (2023)
# https://www.udemy.com/course/avecoder-advanced-python/
# Ave Coder, 2023
# **************************************************************
# Writing by sgiman, May 2025

import time

# decorator 1
def log_function(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with arguments {args} and keyword arguments {kwargs}")
        return func(*args, **kwargs)
    return wrapper

# decorator 2
def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} took {end - start:.6f} seconds to run")
        return result
    return wrapper


@log_function   # decorator 1 (exec 2)
@measure_time   # decorator 2 (exec 1)
def add(x, y):
    return x + y


#####################################################################
print('=' * 80)
print(add(1 ,2))



