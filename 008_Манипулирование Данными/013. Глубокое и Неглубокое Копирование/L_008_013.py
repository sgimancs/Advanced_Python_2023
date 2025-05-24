#! python
# coding=utf-8
# **************************************************************
# L_008_013.py
# 008.Манипулирование Данными
# 013.Глубокое и Неглубокое Копирование
# --------------------------------------------------------------
# Практический Курс по Продвинутому Python (2023)
# https://www.udemy.com/course/avecoder-advanced-python/
# Ave Coder, 2023
# **************************************************************
# Writing by sgiman, May 2025

import copy


print('=' * 80)
list_one = [[1, 2, 3], [4, 5, 6], [7, 8, 'x']]
list_two = list_one     # указатель
print(list_one)

list_two[2][2] = 9

print('=' * 80)
print('List One:', list_one)
print('ID of List One:', id(list_one))

print('List Two:', list_two)
print('ID of List Two:', id(list_two))

############# SHALLOW COPY #############
# Не глубокое (мелкое) копирование
print('=' * 80)

list_one = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list_two = copy.copy(list_one)

print('############# SHALLOW COPY #############')
print('list One:', list_one)
print('list two:', list_two)

list_one.append([10, 11, 12])

print('-' * 80)
print('list One:', list_one)
print('list two:', list_two)    # без изменений

list_one[3][2] = 'X'           # изменения только в оригинале - list_one
print('-' * 80)
print('list One:', list_one)
print('list two:', list_two)    # без изменений

list_one[0][1] = 'Y'

print('-' * 80)
print('list One:', list_one)
print('list two:', list_two)   # изменение в исходных данных

############## DEEP COPY ###############
# Глубокое копирование

list_one = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list_two = copy.deepcopy(list_one)

print('=' * 80)
print('Deep list One:', list_one)
print('Deep list two:', list_two)

list_one[0][1] = 'Y'
print('-' * 80)
print('Deep list One:', list_one)
print('Deep list two:', list_two)   # скопированный постоянно неизменный

