#! python
# coding=utf-8
# **************************************************************
# L_007_011.py
# 007.Итераторы и Генераторы
# 011.Функция zip()
# --------------------------------------------------------------
# Практический Курс по Продвинутому Python (2023)
# https://www.udemy.com/course/avecoder-advanced-python/
# Ave Coder, 2023
# **************************************************************
# Writing by sgiman, May 2025

from itertools import zip_longest


countries = ['Switzerland', 'Estonia', 'Sweden', 'Latvia', 'Butan', 'Nepal']
capitals = ['Bern', 'Tallin', 'Stockholm', 'Riga', 'Thimphu', 'Kathmandu']
capitals2 = ['Bern', 'Tallin', 'Stockholm', 'Riga']

print('=' * 80)
for country, capital in zip(countries, capitals):
    print(f'{capital} is the capital of {country}')

# С недостающими столицами
print('=' * 80)
for country, capital in zip(countries, capitals2):
    print(f'{capital} is the capital of {country}')

# zip_longest ('Unknown')
print('=' * 80)
for country, capital in zip_longest(countries, capitals2, fillvalue='Unknown'):
    print(f'{capital} is the capital of {country}')

