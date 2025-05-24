#! python
# coding=utf-8
# **************************************************************
# L_011_011.py
# 011_Рекурсия
# 003.Факториал (код)
# --------------------------------------------------------------
# Практический Курс по Продвинутому Python (2023)
# https://www.udemy.com/course/avecoder-advanced-python/
# Ave Coder, 2023
# **************************************************************
# Writing by sgiman, May 2025

################################################################
# STANDARD
def factorial1(num):
    return_value = 1
    for i in range(2, num+1):
        return_value *= i
    return return_value

################################################################
# РЕКУРСИЯ
def factorial2(num):
    return 1 if num <= 1 else num * factorial2(num-1)

################################################################
# DEBUG
def factorial3(num):
    print(f'call factorial() with num == {num}')
    return_val =  1 if num <= 1 else num * factorial3(num - 1)
    print(f'factorial({num}) returned {return_val}')
    return return_val

################################################################
# REDUCE/LAMBDA (медленный вариант)
from functools import reduce

def factorial4(num):
    return reduce(lambda a,b: a * b, range(1, num + 1) or [1])


#=========================
# S-T-A-R-T
#=========================
if __name__=='__main__':
    print('=' * 80)
    print(factorial1(5))
    print('=' * 80)
    print(factorial2(5))
    print('=' * 80)
    print(factorial3(5))
    print('=' * 80)
    print(factorial4(5))


