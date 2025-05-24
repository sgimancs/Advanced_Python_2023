#! python
# coding=utf-8
# **************************************************************
# L_012_001_3.py
# 012.Декораторы
# 001.Знакомство с Декораторами
# --------------------------------------------------------------
# Практический Курс по Продвинутому Python (2023)
# https://www.udemy.com/course/avecoder-advanced-python/
# Ave Coder, 2023
# **************************************************************
# Writing by sgiman, May 2025

import time

# ДЕКОРАТОР
def log_execution_time(log_level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            result = func(*args, **kwargs)
            end_time = time.perf_counter()
            execution_time = end_time - start_time
            print(f"{log_level}: {func.__name__} took {execution_time: .6f} seconds to execute")
            return result
        return wrapper
    return decorator


# Применить декоратор
@log_execution_time("INFO")
def add(x, y):
    time.sleep(1)
    return x + y


################################################################
print('=' * 80)

result = add(2,3)
print(result)




