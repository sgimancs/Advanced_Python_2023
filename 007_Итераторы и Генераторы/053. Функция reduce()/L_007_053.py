#! python
# coding=utf-8
# **************************************************************
# L_007_053.py
# 007.Итераторы и Генераторы
# 053.Функция reduce()
# --------------------------------------------------------------
# Практический Курс по Продвинутому Python (2023)
# https://www.udemy.com/course/avecoder-advanced-python/
# Ave Coder, 2023
# **************************************************************
# Writing by sgiman, May 2025

import functools
from functools import reduce
from operator import add
from operator import mul
from timeit import timeit

from numpy.random.mtrand import operator

nums = [1, 2, 3, 4, 5,]

###### REDUCE MECHANICS ######
# function.reduce(function, iterable[, initializer])
# def reduce(function, iterable, initializer=None):
#     it = iter(iterable)
#     if initializer is None:
#         value = next(it)
#     for element in it:
#         value = function(value, element)
#     return value

##################################################################
print('=' * 80)
def sgi_add(a,b):
    result = a +b
    print(f"{a} + {b} = {result}")
    return result

print(sgi_add(2, 4))

print('=' * 80)
print(reduce(sgi_add, nums))        # сумма чисел в списке

############ initializer & lambda ############
print('=' * 80)
print(reduce(sgi_add, nums, 1000))  # сумма чисел списка с начального значения = 1000

print('=' * 80)
print('LAMBDA SUM:', reduce(lambda a, b: a + b, nums)) # сумма чисел списка c помощью lambda

print('=' * 80)
print('LAMBDA SUM:', reduce(lambda a, b: a + b, nums, 1000))

########### add ###########

print('=' * 80)
print(add(2,3))

print('=' * 80)
print('ADD:', reduce(add, nums))            # 15

print('=' * 80)
print('ADD:', reduce(add, nums, 1000))      # 1015


########### sum ###########
# Суммирование элементов списка
print('=' * 80)
print('SUM:', sum(nums))


########### mult nums ###########
# Умножение элементов списка
print('=' * 80)

def sgi_mult_list(product, nlist):
    for num in nlist:
        product *= num
    return product

def sgi_mult(a, b):
    return a * b

print(sgi_mult_list(1, nums))     # sgi_mult_list
print(reduce(sgi_mult, nums))             # reduce/sgi_mult
print(reduce(lambda a, b: a * b, nums))   # reduce/lambda

# Умножение mul
print('=' * 80)
print(mul(4, 5))       # скалярные значения

print('=' * 80)
print(reduce(mul, nums))    # список nums

#******************************************************
# TIME EXEC (OPTIMISATION)
#******************************************************
print('*' * 80)
# func
def add(a, b):
    return a + b

sgi_add = "functools.reduce(add, range(100))"
print(timeit(sgi_add, "import functools", globals={'add': add}))    # 10.711247899991577 сек.

# lambda
sgi_lambda = "functools.reduce(lambda x, y: x + y, range(100))"
print(timeit(sgi_lambda,"import functools"))                    # 10.748262799999793 сек.

# operator.add
operator_add = "functools.reduce(operator.add, range(100))"
print(timeit(operator_add, "import functools, operator"))   # 5.191780900000595 сек.
# sum
print(timeit("sum(range(100))", globals={"sum":sum}))       # 1.132688900004723 сек.
