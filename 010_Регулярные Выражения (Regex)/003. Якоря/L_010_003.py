#! python
# coding=utf-8
# **************************************************************
# L_009_003.py
# 010.Регулярные Выражения (Regex)
# 003.Якоря
# --------------------------------------------------------------
# Практический Курс по Продвинутому Python (2023)
# https://www.udemy.com/course/avecoder-advanced-python/
# Ave Coder, 2023
# **************************************************************
# Writing by sgiman, May 2025

import re

### ^ ### \A ###
print('=' * 80)
print(re.search('^ave', 'avecoder'))    # поиск только в начале
print(re.search('^ave', 'coderave'))

print(re.search(r'\Aave', 'avecoder'))  # поиск только в начале

### $ ### \Z ###
print('=' * 80)
print(re.search(r'coder$', 'avecoder'))
print(re.search(r'coder$', 'coderave'))

print(re.search(r'coder\Z', 'avecoder')) # ???
print(re.search(r'coder\Z', 'coderave')) # ???

###### \b
print('=' * 80)
print(re.search(r'\bcoder', 'ave coder'))
print(re.search(r'\bcoder', 'ave.coder'))
print(re.search(r'\bcoder', 'avecoder'))

print('-' * 80)
print(re.search(r'coder\b', 'ave coder'))
print(re.search(r'coder\b', 'ave.coder'))
print(re.search(r'coder\b', 'avecoder'))

print('-' * 80)
print(re.search(r'\bcoder\b', 'ave coder moder'))
print(re.search(r'\bcoder\b', 'ave(coder)moder'))
print(re.search(r'\bcoder\b', 'avecodermoder'))

###### \B
print('=' * 80)
print(re.search(r'\Bcoder\B', 'coder'))             # -
print(re.search(r'\Bcoder\B', '.coder.'))           # -
print(re.search(r'\Bcoder\B', 'ave coder moder'))   # -
print(re.search(r'\Bcoder\B', 'avecodermoder'))     # + (без разделителя)
