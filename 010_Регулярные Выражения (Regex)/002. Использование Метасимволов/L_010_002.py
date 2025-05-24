#! python
# coding=utf-8
# **************************************************************
# L_009_012.py
# 010.Регулярные Выражения (Regex)
# 002.Использование Метасимволов
# --------------------------------------------------------------
# Практический Курс по Продвинутому Python (2023)
# https://www.udemy.com/course/avecoder-advanced-python/
# Ave Coder, 2023
# **************************************************************
# Writing by sgiman, May 2025

import re

####### []
print('=' * 80)
print(re.search('co[dn]e', 'avecoder'))     # +
print(re.search('co[tn]e', 'avecoder'))     # -
print(re.search('co[dn]e', 'cones'))        # +

#################################################################
print('=' * 80)
print(re.search('[a-z]', 'avecoder'))   # первое совпадение по одиночному символу
print(re.search('[A-Z]', 'aVecoder'))
print(re.search('[0-9]', '000avecoder'))

######## ^
# ^ - отрицание
print('=' * 80)
print(re.search('[^0-9]', '000avecoder'))

# Для поиска дефиса "-"
print(re.search('[-ave]', '000-ave'))
print(re.search('[ave-]', '000-ave'))
print(re.search(r'[a\-ve]', '000-ave'))

######## ]
print('=' * 80)
print(re.search('[]]', 'ave :]'))
print(re.search(r'[\\]]', 'ave :]'))

######## (.)
# "." - любой символ
print('=' * 80)
print(re.search('av.coder', 'avecoder'))
print(re.search('ave.coder', 'avecoder'))

####### \w == [a-zA-Z0-9_] - найти всё по шаблону
# Буквы и Цифры
print('=' * 80)
print(re.search(r'\w', 'avecoder'))  # ??? (SyntaxWarning: invalid escape sequence)
print(re.search(r'\w', '.v-#?/]|[')) # ??? (SyntaxWarning: invalid escape sequence)

####### \W = [^a-zA-Z0-9_] - найти кроме ...
print('=' * 80)
print(re.search(r'\W', '.v-#?/]|[')) # ??? (SyntaxWarning: invalid escape sequence)
print(re.search(r'\W', 'a*ecoder'))

######## \d
# числа
print('=' * 80)
print(re.search(r'\d', 'av3ecoder'))

######## \D
# не числа
print('=' * 80)
print(re.search(r'\D', '1234O0'))

######## \s
# пробелы
print('=' * 80)
print(re.search(r'\s', 'ave coder'))

######## \S
# не пробелы
print('=' * 80)
print(re.search(r'\S', '      |      '))

##############################################################
# комбинирование метасимволов
print('=' * 80)
print(re.search(r'[\d\w\s]', '-------0-------'))

######## \
print(re.search(r'\.', 'avecoder.com'))

rs = r'directory\folder'            # сырая строка
print(re.search(r"\\", rs))
print(re.search(r'\\\\', rs))  # ????



