#! python
# coding=utf-8
# **************************************************************
# L_007_072.py
# 007.Итераторы и Генераторы
# 072.Функция filter()
# --------------------------------------------------------------
# Практический Курс по Продвинутому Python (2023)
# https://www.udemy.com/course/avecoder-advanced-python/
# Ave Coder, 2023
# **************************************************************
# Writing by sgiman, May 2025

import math

nums = [-5, 0, 1, 3, -4, -6, 9, -7, 2, 4, 2, 4, 5]


def filter_negatives(lnums):
    neg_n = []
    for n in lnums:
        if n < 0:                   # если отрицательные
            neg_n.append(n)
    return neg_n


if __name__ == "__main__":
    print('=' * 80)
    print(filter_negatives(nums))


################################################################
####### filter(function, iterable)
# filter(func, array)

# LAMBDA
print('=' * 80)
neg_nums = filter(lambda x: x < 0, nums)
print(list(neg_nums))

# FUNCTION
print('=' * 80)
def is_negaive(num):
    return num < 0

if __name__ == "__main__":
    print(list(filter(is_negaive, nums)))


################################################################
####### filter() + map()

def is_negative(num):
    return num < 0

neg_nums = list(filter(is_negative, nums))

print('=' * 80)
print(neg_nums)

# LONG CODE
print(list (map (lambda n: math.sqrt(math.pow(n, 2)), neg_nums) ) )
print(list(map(lambda n: math.sqrt(math.pow(n, 2)), filter(is_negaive, nums))))


################################################################
####### filter() + map() + reduce()

from functools import reduce

print('=' * 80)

def is_negative(num):
    return num < 0

negs_nums = list(filter(is_negative, nums))
print(reduce(lambda a, b: a * b, neg_nums))
print(reduce(lambda a,b: a * b, filter(is_negaive, nums)))  # мощный однострочник (фильтрация)


################################################################
####### filterfalse() - элементы которые не прошли фильтрацию
print('=' * 80)

from itertools import filterfalse

def is_negative(num):
    return  num < 0

print(list(filterfalse(is_negative, nums)))
print('=' * 80)


