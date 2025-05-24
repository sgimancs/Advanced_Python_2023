#! python
# coding=utf-8
# **************************************************************
# L_007_001.py
# 007.Итераторы и Генераторы
# 001.Энумератор (enumerate)
# --------------------------------------------------------------
# Практический Курс по Продвинутому Python (2023)
# https://www.udemy.com/course/avecoder-advanced-python/
# Ave Coder, 2023
# **************************************************************
# Writing by sgiman, May 2025


countries = ['Switzerland', 'Estonia', 'Sweden', 'Latvia', 'Butan', 'Nepal']

################################################################
# STRINGS
print('=' * 80)
for index in range(len(countries)):
    print(f'{index+1}, {countries[index]}')

################################################################
# КОРТЕЖ (пронумеровать - enumerate)
print('=' * 80)
for item in enumerate(countries, start=1):
    print(item)

# Разделить кортеж (with place-holder "{}")
print('=' * 80)
for index, country in enumerate(countries, start=1):
    print(f'{index}, {country}')
