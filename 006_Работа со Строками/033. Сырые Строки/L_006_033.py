#! python
# coding=utf-8
# **************************************************************
# L_006_033.py
# 006_Работа со Строками
# 033.Сырые Строки
# --------------------------------------------------------------
# Практический Курс по Продвинутому Python (2023)
# https://www.udemy.com/course/avecoder-advanced-python/
# Ave Coder, 2023
# **************************************************************
# Writing by sgiman, May 2025

import string

print('=' * 80)
not_raw_str = "Not\tRaw\nString"
print(not_raw_str)

print('=' * 80)
raw_str = r"Not\tRaw\nString"   # сырая строка с игнорированием формата ESC-символов
print(raw_str)
print(not_raw_str)

print('=' * 80)
print(type(not_raw_str))
print(type(raw_str))

print('=' * 80)
print(r'Not\tRaw\nString' == 'Not\\tRaw\\nString')  # True (с экранирующим двойным slash)

print('=' * 80)
print(len(not_raw_str))
print(len(raw_str))

print('=' * 80)
print(list(not_raw_str))
print(list(raw_str))

#############################################################
print('=' * 80)
path = 'C:\\Windows\\system32\\cmd.exe'
rpath = r'C:\Windows\system32\cmd.exe'
print(path)
print(rpath)
print(path == rpath)

print('=' * 80)
path2 = 'C:\\Windows\\system32\\'
rpath2 = r'C:\Windows\system32\\'
rpath2 = r'C:\Windows\system32' + '\\'
print(path2 == rpath2)

############################################################
print('=' * 80)
s_r = repr(not_raw_str) # эквивалент сырой строки
print(s_r)
print(list(s_r))

print('=' * 80)
s_r2 = repr(not_raw_str)[1:-1]  # избавиться от ограничивающих кавычек с помощью срезов
print(s_r2)
print(raw_str == s_r2)

print('=' * 80)
print(r'\t' == repr('\t')[1:-1])
