#! python
# coding=utf-8
# **************************************************************
# L_009_001.py
# 010.Регулярные Выражения (Regex)
# 001.Функция Поиска по Совпадению
# --------------------------------------------------------------
# Практический Курс по Продвинутому Python (2023)
# https://www.udemy.com/course/avecoder-advanced-python/
# Ave Coder, 2023
# **************************************************************
# Writing by sgiman, May 2025

import re   # регулярные выражения

s = "egg000ham"

zeros = re.search('000', s)

print('=' * 80)
print(zeros)

if zeros:
    print('Match')
else:
    print('No Match')

################################################################
print('=' * 80)

# Найти по шаблону (паттерну)
print(re.search('[0-9][0-9][0-9]', 'egg000ham'))
print(re.search('[0-9][0-9][0-9]', '000eggham'))
print(re.search('[0-9][0-9][0-9]', 'eggham000'))
print(re.search('[0-9][0-9][0-9]', '00eggham0'))

# '.' искать для всех
print('=' * 80)

s = "egg000ham"
print(re.search('0.0', s))  # совпадения
s = "00eggham"
print(re.search('0.', s))   # совпадения
