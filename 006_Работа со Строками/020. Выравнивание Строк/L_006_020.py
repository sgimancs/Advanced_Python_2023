#! python
# coding=utf-8
# **************************************************************
# L_006_020.py
# 006_Работа со Строками
# 020.Выравнивание Строк
# --------------------------------------------------------------
# Практический Курс по Продвинутому Python (2023)
# https://www.udemy.com/course/avecoder-advanced-python/
# Ave Coder, 2023
# **************************************************************
# Writing by sgiman, May 2025

import string

#
# The 7 dwarfs names are Happy, Doc, Grumpy, Dopey, Bashful, Sleepy,
# and Sneezy from the Disney movie Snow White and the Seven Dwarfs.
#
names = ["Doc", "Grumpy", "Bashful", "Sleepy", "Happy", "Sneezy", "Dopey"]
longest = max(len(name) for name in names)

# Выравнивание по левому краю (LJUST)
print('=' * 80)
for name in names:
    print(name.ljust(longest+2, "-") + ":")

# Выравнивание по центру (CENTER)
print('=' * 80)
for name in names:
    print(name.center(longest+2, "-") + ":")

# Выравнивание по правому краю (RJUST)
print('=' * 80)
for name in names:
    print(name.rjust(longest+2, "-") + ":")
