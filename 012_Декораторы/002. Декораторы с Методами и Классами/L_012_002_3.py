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
from scipy.sparse.csgraph import depth_first_tree


# =======================
#  ДЕКОРАТОРЫ - КЛАССЫ
# =======================

# -----------------------
# MyDecorator (CLASS)
# -----------------------
class MyDecorator:
    # Constructor
    def __init__(self, func):
        self.func = func

    # CALL
    def __call__(self, *args, **kwargs):
        # Do something before
        print("John enters the room")           # before
        result = self.func(*args, **kwargs)     # func
        # Do somthing after
        print("John leaves the room")           # after
        return result


# -----------------------
#  greet()
# -----------------------
@MyDecorator
def greet(name):
    print("Hello. " + name + "!")


########################################################
print('=' * 80)
greet("John")
