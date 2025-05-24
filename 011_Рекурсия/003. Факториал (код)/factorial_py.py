#! python
# coding=utf-8
# **************************************************************
# factorial_py.py
# 011_Рекурсия
# 003.Факториал (код)
# --------------------------------------------------------------
# Практический Курс по Продвинутому Python (2023)
# https://www.udemy.com/course/avecoder-advanced-python/
# Ave Coder, 2023
# **************************************************************
# Writing by sgiman, May 2025

# PYTHON FACTORIAL (MATH) - самый быстрый вариант

from timeit import timeit

#################################################################
### recursive

stmt = '''def factorial(num):
            return 1 if num <=1 else num * factorial(num-1)              
'''

print('=' * 80)
print('Recursive: ', timeit('factorial(5)', setup=stmt, number=1000000))


#################################################################
### iterative

stmt = '''def factorial(num):
            return_val = 1
            for i in range(2, num + 1):
                return_val *= i
            return return_val                
       '''

print('=' * 80)
print('Iterative: ', timeit('factorial(5)', setup=stmt, number=1000000))


#################################################################
### reduce

stmt = '''
from functools import reduce
def factorial(num):
    return reduce(lambda a,b: a * b, range(1, num + 1) or [1]) 
'''

print('=' * 80)
print('Reduce: ', timeit('factorial(5)', setup=stmt, number=1000000))

#################################################################
### math
stmt = 'from math import factorial'

print('=' * 80)
print('Math: ', timeit('factorial(5)', setup=stmt, number=1000000))

