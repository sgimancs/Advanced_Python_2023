#! python
# coding=utf-8
# **************************************************************
# L_005_001.py
# 005.Comprehensions (Генераторы Списков, Множеств, Словарей)
# 001.List Comprehensions (Генераторы Списков)
# --------------------------------------------------------------
# Практический Курс по Продвинутому Python (2023)
# https://www.udemy.com/course/avecoder-advanced-python/
# Ave Coder, 2023
# **************************************************************
# Writing by sgiman, May 2025

# Comprehensions - Понимание

numbers = [0,  1, 2, 3, 4, 5, 6, 7, 8, 9]

#==============================================================
#### for loop ####
print('-' * 80)
squares = []
for number in numbers:
    squares.append(number**2)
print(squares)

print('-' * 80)
squares = [number**2 for number in numbers]     # генератор списка
print(squares)

#==============================================================
####### list comp cond ######
print('-' * 80)
evens = [number for number in numbers if number % 2 == 0]      # чётные числа
print('evens: ', evens)

#==============================================================
####### list comp pairs ######
print('-' * 80)
numbers1 = [0, 1, 2, 3]
numbers2 = [4, 5, 6, 7]

pairs = [(number1, number2) for number1 in numbers1 if number1 % 2 == 0
         for number2 in numbers2 if number2 % 2 == 1]

print(pairs)

#==============================================================
####### list comp range ######
print('-' * 80)
lists = [[i  for i in range(j)] for j in range(5)]
print('lists: ', lists)







