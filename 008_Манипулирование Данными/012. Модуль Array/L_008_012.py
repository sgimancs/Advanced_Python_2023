#! python
# coding=utf-8
# **************************************************************
# L_008_012.py
# 008.Манипулирование Данными
# 012.Модуль Array
# --------------------------------------------------------------
# Практический Курс по Продвинутому Python (2023)
# https://www.udemy.com/course/avecoder-advanced-python/
# Ave Coder, 2023
# **************************************************************
# Writing by sgiman, May 2025

from array import array

int_array = array('i', [18, 6, 21, 20, 43, 22, 33, 60, 8, 4, 3, 6, 16, 31, 34])
print('=' * 80)
print(int_array)

print(int_array.typecode)   # код типа 'i' (целые числа)
print(int_array.itemsize)   # размер = 4 байта

################################################################
int_array.insert(0,0)   # вставить в начало
int_array.append(42)          # давить в конец
int_array.extend([35,36,37])  # расширить массив

print('=' * 80)
print(int_array)

# Пронумеровать(проиндексировать) и обработать массив
for i, elem in enumerate(int_array):
    int_array[i] = elem * 2

print(int_array)

################################################################
# ERROR!!!
# print('=' * 80)
# int_array.insert(0,5.5)   # вставить в начало

