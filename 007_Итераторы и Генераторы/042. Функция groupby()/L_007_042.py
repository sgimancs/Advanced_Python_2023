#! python
# coding=utf-8
# **************************************************************
# L_007_042.py
# 007.Итераторы и Генераторы
# 042.Функция groupby()
# --------------------------------------------------------------
# Практический Курс по Продвинутому Python (2023)
# https://www.udemy.com/course/avecoder-advanced-python/
# Ave Coder, 2023
# **************************************************************
# Writing by sgiman, May 2025

import itertools

#***************************************************************
# СГРУППИРОВАТЬ (groupby)
#***************************************************************

num_list = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4,]
print('+' * 80)
print(itertools.groupby(num_list))
for i, j in itertools.groupby(num_list):
    print("i: ", i, "j: ", list(j))

################################################################
print('+' * 80)
print([i for i, j in itertools.groupby(num_list)])              # элементы без дублей (ключи)
print([list(j) for i, j in itertools.groupby(num_list)])        # списки дублей (значения)
print([(i, list(j)) for i, j in itertools.groupby(num_list)])   # элементы и списки дублей (ключи и значения)

################################################################
print('+' * 80)
print('LAMBDA')
print([(i, list(j)) for i, j in itertools.groupby(num_list, lambda x: x * 2)]) # ключи * 2

################################################################
# СПИСКИ
data = [[0, 'Egg', 10],
        [1, 'Egg', 20],
        [2, 'Ham', 30],
        [2, 'Ham', 40],
        [2, 'Ham', 50]]

print('+' * 80)

# Сгруппировать по значению среднего столбца
for i, j in itertools.groupby(data, lambda x: x[1]):
    print(i, list(j))

################################################################
# КОРТЕЖИ И СТРОКИ
print('+' * 80)
tpl = (1,1,1,2,2,2,3,3,3,4,4,4,)
print('TUPLE')
print([(i, list(j)) for i, j in itertools.groupby(tpl)])        # список кортежей
print(tuple((i, tuple(j)) for i, j in itertools.groupby(tpl) )) # кортеж кортежей

################################################################
print('+' * 80)
s = "xxxyyyzzz"

print('STRING')

print([(i, list(j)) for i, j in itertools.groupby(s)])
