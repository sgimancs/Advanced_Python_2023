#! python
# coding=utf-8
# **************************************************************
# L_009_006.py
# 010.Регулярные Выражения (Regex)
# 006.Механизмы Lookahead и Lookbehind
# --------------------------------------------------------------
# Практический Курс по Продвинутому Python (2023)
# https://www.udemy.com/course/avecoder-advanced-python/
# Ave Coder, 2023
# **************************************************************
# Writing by sgiman, May 2025

import re

###### (?=<lookahead_regex>)
# Позитивный поиск
print(re.search('ave(?=[a-z])', 'avecoder'))
print(re.search('ave(?=[a-z])', 'ave000coder'))
print(re.search('ave([a-z])', 'avecoder'))

###### (?!<lookhead_regex>)
# Негативный поиск
print(re.search('ave(?=[a-z])', 'avecoder'))
print(re.search('ave(?![a-z])', 'ave000coder'))
print(re.search('ave(?![a-z])', 'avecoder000'))     # None

###### (?<=<lookbehind_regex>)
# Поиск назад - стрелка влево (<=)

print(re.search('(?<=ave)coder', 'avecoder'))
print(re.search('(?<=coder)ave', 'avecoder'))
print(re.search('(?<=a{5})ve', 'aaaaave'))

###### (?!<=<lookbehind_regex>)
# Негативный респрективный поиск
print(re.search('(?<!ave)coder', 'avecoder'))   # None
print(re.search('(?<!ave)ave', 'avecoder'))     # +

