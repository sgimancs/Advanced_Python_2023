#! python
# coding=utf-8
# **************************************************************
# L_012_002.py
# 012.Декораторы
# 002.Декораторы с Методами и Классами
# --------------------------------------------------------------
# Практический Курс по Продвинутому Python (2023)
# https://www.udemy.com/course/avecoder-advanced-python/
# Ave Coder, 2023
# **************************************************************
# Writing by sgiman, May 2025

import time

# ----------------------------------
#  log_execution_time() - decorator
# ----------------------------------
def log_execution_time(func):
    def wrapper(self, *args, **kwargs):
        start_time = time.perf_counter()
        result = func(self, *args, **kwargs)
        end_time = time.perf_counter()
        executive_time = end_time - start_time
        print(f"{self.__class__.__name__}: {func.__name__} took {executive_time:.6f} seconds to execute")
        return result
    return wrapper


# ****************************
#  Calculator (CLASS)
# ****************************
class Calculator:
    # Constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Method
    @log_execution_time
    def add(self):
        time.sleep(1)
        return self.x + self.y


########################################################
print('=' * 80)

calculator = Calculator(2, 3)   # object
result = calculator.add()
print(result)
