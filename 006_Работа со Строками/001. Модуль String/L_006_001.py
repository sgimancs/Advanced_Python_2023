#! python
# coding=utf-8
# **************************************************************
# L_006_001.py
# 006_Работа со Строками
# 001.Модуль String
# --------------------------------------------------------------
# Практический Курс по Продвинутому Python (2023)
# https://www.udemy.com/course/avecoder-advanced-python/
# Ave Coder, 2023
# **************************************************************
# Writing by sgiman, May 2025

import string

# print('-' * 80)
# print(string.ascii_letters)     # ascii chars
# print(string.punctuation)       # символы
# print(string.hexdigits)         # 16-ти ричные символы
# print(string.digits)            # цифры

print('-' * 80)
# "Ракушки, которые она продаёт, — это морские ракушки."
test_str1 = 'The shells she sells are sea-shells'
test_str2 = 'IntegragallaticPython'
#test_str2 = 'IntegragallaticPython5'
test_str3 = '419209'

# Пробел - не буква...
res = "".join([c for c in test_str1 if c in string.ascii_letters])  # строка без пробелов
print(res)

print('-' * 80)
print(all([c.isalpha() for c in test_str1]))
print(test_str1.isnumeric())
print(test_str3.isnumeric())

# print('-' * 80)
# print(test_str1.isalnum())  # буквы и цифры
# print(test_str2.isalpha())  # буквы




