#! python
# coding=utf-8
# ********************************************************
# L_001_001.py
# 001.Разогрев
# 001.Знакомство с модулем math
# --------------------------------------------------------
# Практический Курс по Продвинутому Python (2023)
# https://www.udemy.com/course/avecoder-advanced-python/
# Ave Coder, 2023
# ********************************************************
# Writing by sgiman, May 2025

import math

print('-' * 80)
print(math.pi)      # чиcло PI (3.141592653589793)
print(math.e)       # число эулера (2.718281828459045)
print('-' * 80)


print(math.nan)
print(math.inf)
print(-math.inf)
print('-' * 80)


direction = math.cos(math.pi / 4)   # COS
print(direction)
print(math.sin(math.pi / 4))        # SIN
print('-' * 80)


man = 2.5
print(math.ceil(man))       # CEIL  - округление вверх
print(math.floor(man))      # FLOOR - округление вниз
print('-' * 80)
