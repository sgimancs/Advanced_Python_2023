#! python
# coding=utf-8
# **************************************************************
# L_009_004.py
# 010.Регулярные Выражения (Regex)
# 004.Квантификаторы
# --------------------------------------------------------------
# Практический Курс по Продвинутому Python (2023)
# https://www.udemy.com/course/avecoder-advanced-python/
# Ave Coder, 2023
# **************************************************************
# Writing by sgiman, May 2025

import re

###### *
print("=" * 80)
print(re.search('ave-*coder', 'avecoder'))
print(re.search('ave-*coder', 'ave-coder'))
print(re.search('ave-*coder', 'ave--coder'))

###### +
print("=" * 80)
print(re.search('ave-+coder', 'avecoder'))
print(re.search('ave-+coder', 'ave-coder'))
print(re.search('ave-+coder', 'ave--coder'))

###### ?
print("=" * 80)
print(re.search('ave-?coder', 'avecoder'))
print(re.search('ave-?coder', 'ave-coder'))
print(re.search('ave-?coder', 'ave--coder'))    # только для единичного совпадения

###### *? +? ??
print("=" * 80)
print(re.search('<.*>', '<coder> <coderz>%'))   # один и более совпадений
print(re.search('<.*?>', '<coder> <coderz>%'))  # ограничить
print(re.search('<.+>', '<coder> <coderz>%'))   # более...
print(re.search('<.+?>', '<coder> <coderz>%'))   # минимальное совпадение

print(re.search('av?', 'ave'))
print(re.search('av??', 'aveeeee'))

###### {m}
print("=" * 80)
print(re.search('x-{3}x', 'x--x'))      # -
print(re.search('x-{3}x', 'x---x'))     # + совпадение
print(re.search('x-{3}x', 'x----x'))    # -

###### {m,n} - интервал в паттерне
print("=" * 80)
for i in range(1, 10):
    s = f"x{'-' * i}x"
    print(f'{i} {s:10}', re.search('x-{2,5}x', s))
