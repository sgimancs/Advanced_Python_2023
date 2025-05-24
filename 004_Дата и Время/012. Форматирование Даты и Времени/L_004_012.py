#! python
# coding=utf-8
# ********************************************************
# L_004_012.py
# 004.Дата и Время
# 012.Форматирование Даты и Времени
# --------------------------------------------------------
# Практический Курс по Продвинутому Python (2023)
# https://www.udemy.com/course/avecoder-advanced-python/
# Ave Coder, 2023
# ********************************************************
# Writing by sgiman, May 2025

from datetime import date, time, datetime


now = datetime.now()

# Current Time
print('-' * 80)
print(now)

# Days
print('-' * 80)
print(now.strftime("%a, %A, %w, %d"))

# Months
print('-' * 80)
print(now.strftime("%b, %B, %m"))

# Time
print('-' * 80)
print(now.strftime("%H, %I, %M, %S, %p"))

# Local time
print('-' * 80)
print(now.strftime("%c"))
print('-' * 80)

