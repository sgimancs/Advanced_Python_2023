#! python
# coding=utf-8
################################################################################################
# for_iterate.py
# Итерация с помощью циклов for
# https://proglib.io/p/python-enumerate-uproshchaem-cikly-s-pomoshchyu-schetchikov-2020-12-08
################################################################################################
# Writing by sgiman, May 2025

values = ["a", "b", "c"]

#========================================================================#
###### Sample 1 ######
print('=' * 80)
for value in values:
    print(value)
"""
a
b
c
"""


#========================================================================#
###### Sample 2 ######
print('=' * 80)
index = 0
for value in values:
    print('index: ', index, value)
    index += 1
"""
0 a
1 b
2 c
"""


#========================================================================#
###### Sample 3 ######
print('=' * 80)
for index in range(len(values)):
    value = values[index]
    print('range: ', index, value)
"""
0 a
1 b
2 c
"""

#========================================================================#
###### Sample 4 ######
# enumerate  возвращает две переменные цикла:
# количество текущих итераций и значение элемента на текущей итерации.
print('=' * 80)
for count, value in enumerate(values):
    print('enumerate: ', count, value)
"""
0 a
1 b
2 c
"""

#========================================================================#
###### Sample 5 ######
# enumerate: index & element (return)
print('=' * 80)
users = ["Test User", "Real User 1", "Real User 2"]
for index, user in enumerate(users):
    if index == 0:
        print("Вывод для:", user)
    print(user)
"""
Вывод для: Test User
Real User 1
Real User 2
"""

#========================================================================#
###### Sample 6 ######
# even_items:  принимает аргумент iterable.
print('=' * 80)

def even_items(iterable):
    """Возврат элементов ``iterable`` когда индекс четный"""
    values = []
    for index, value in enumerate(iterable, start=1):
        if not index % 2:           # если index четный
            values.append(value)    # заполнить список
        return values

seq = list(range(1, 11))
print(seq)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_items(seq)
# [2, 4, 6, 8, 10]

#========================================================================#
###### Sample 7 ######
# list comprehension
print('=' * 80)

def even_items(iterable):
    return [v for i, v in enumerate(iterable, start=1) if not i % 2]

seq = list(range(1, 11))
print(seq)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(even_items(seq))
#[2, 4, 6, 8, 10]

alphabet = "abcdefghijklmnopqrstuvwxyz"
print(even_items(alphabet))
# ['b', 'd', 'f', 'h', 'j', 'l', 'n', 'p', 'r', 't', 'v', 'x', 'z']

#========================================================================#
print('=' * 80)
