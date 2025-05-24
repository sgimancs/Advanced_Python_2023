#! python
# coding=utf-8
# **************************************************************
# L_006_006.py
# 006_Работа со Строками
# 006.Поиск в Строке
# --------------------------------------------------------------
# Практический Курс по Продвинутому Python (2023)
# https://www.udemy.com/course/avecoder-advanced-python/
# Ave Coder, 2023
# **************************************************************
# Writing by sgiman, May 2025

import string

#############################################################################
# "Питер Пайпер собрал кучу маринованного перца"
sample_str = 'Peter Piper picked a peck of pickled pepper'

print('-' * 80)

print(sample_str.startswith('Peter'))
print(sample_str.startswith('peter'))
print(sample_str.endswith('pepper'))

print('-' * 80)

# SEARCH - return index string
print(sample_str.find('Peter'))
print(sample_str.rfind('Peter'))

print('-' * 80)
print(sample_str.find('picked'))
print(sample_str.rfind('picked'))

# ПОИСК С ЗАМЕМОЙ
print('-' * 80)
new_str = sample_str.replace('pepper', 'apple')
print(new_str)

# СЧЁТЧИК
print('-' * 80)
print(sample_str.count('a'))
