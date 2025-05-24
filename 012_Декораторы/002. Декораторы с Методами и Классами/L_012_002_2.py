#! python
# coding=utf-8
# **************************************************************
# L_012_002_2.py
# 012.Декораторы
# 002.Декораторы с Методами и Классами
# --------------------------------------------------------------
# Практический Курс по Продвинутому Python (2023)
# https://www.udemy.com/course/avecoder-advanced-python/
# Ave Coder, 2023
# **************************************************************
# Writing by sgiman, May 2025

# =======================
#  ДЕКОРАТОРЫ В КЛАССАХ
# =======================

import time

# ----------------------------------------
#  log_execution_time(CLASS) - decorator
# ----------------------------------------
def log_execution_time(cls):
    class Wrapper(cls):
        def __new__(cls, *args, **kwargs):
            instance = super().__new__(cls)
            instance.start_time = time.perf_counter()
            return instance

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.end_time = time.perf_counter()
            execution_time = self.end_time - self.start_time
            print(f"{cls.__name__}: took {execution_time:.6f} seconds to instantiate")

        def __del__(self):
            end_time = time.perf_counter()
            execution_time = end_time - self.start_time
            print(f"{cls.__name__} took {execution_time:.6f} seconds ti be garbage collected")

    return Wrapper


# ----------------------------------
#  Calculator (CLASS)
# ----------------------------------
@log_execution_time
class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        time.sleep(1)

    def add(self):
        return self.x + self.y


########################################################
print('=' * 80)
calc = Calculator(2,3)     # object
