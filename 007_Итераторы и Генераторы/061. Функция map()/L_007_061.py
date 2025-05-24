#! python
# coding=utf-8
# **************************************************************
# L_007_061.py
# 007.Итераторы и Генераторы
# 061.Функция map()
# --------------------------------------------------------------
# Практический Курс по Продвинутому Python (2023)
# https://www.udemy.com/course/avecoder-advanced-python/
# Ave Coder, 2023
# **************************************************************
# Writing by sgiman, May 2025

import math

def square(n):
    return pow(n, 2)

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # LIST

squared_list = map(square, num_list)            # MAP object / list = map(func, array)
print("=" * 80)
print(squared_list)                             # address object
print(f'squared_list: {list(squared_list)}')    # приведение типов

#################################################################
print("=" * 80)

float_list = [1.23, 2.24, 3.35, 4.46, 5.57, 6.68, 7.79, 8.89, 9.99]

rounded_list = map(round, float_list)
ceiled_list = map(math.ceil, float_list)        # c округлением "потолок"(ceil)
floored_list = map(math.floor, float_list)      # c округлением "пол" (floor)

print(f'rounded_list: {list(rounded_list)}')    # round+
print(f'ceiled_list: {list(ceiled_list)}')      # ceil
print(f'floored_list: {list(floored_list)}')    # floor

#################################################################
print("=" * 80)

my_string = "DADADA DUDUDU DIDIDI"

def lower_char(s):
    return s.lower()

new_str_list = map(lower_char, my_string)       # list = map(func, array)
print(f'new_str_list: {list(new_str_list)}')

##################################################################
print("=" * 80)

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # LIST NUMBER

lambda_list = map(lambda x: x*10, num_list)
print(f'lambda_list: {list(lambda_list)}')

##################################################################
print("=" * 80)

list1 = [2, 2, 2, 2, 2]
list2 = [5, 5, 5, 5, 5]

def mult_func(l1, l2):
    return l1 * l2

mult_list = map(mult_func, list1, list2)
print(f'mult_list: {list(mult_list)}')

##################################################################
print("=" * 80)

tuple1 = "Room", "Room", "Room", "Room",
list1 = ["A", "B", "C", "D"]

def tuple_list_func(tpl, lst):
    return tpl + " - " + lst

room_list = map(tuple_list_func, tuple1, list1)
print(f'room_list: {list(room_list)}')



