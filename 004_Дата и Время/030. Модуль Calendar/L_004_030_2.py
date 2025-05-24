#! python
# coding=utf-8
# ********************************************************
# L_004_030_2.py
# 004.Дата и Время
# 030.Модуль Calendar
# --------------------------------------------------------
# Практический Курс по Продвинутому Python (2023)
# https://www.udemy.com/course/avecoder-advanced-python/
# Ave Coder, 2023
# ********************************************************
# Writing by sgiman, May 2025

import calendar
import pprint


#########################
### Calendar as lists ###

print('-' * 80)
pprint.pprint(calendar.monthcalendar(2025, 1))  # список списков

print('-' * 80)
calendar.setfirstweekday(5)
pprint.pprint(calendar.monthcalendar(2025, 1))

print('-' * 80)
caldr = calendar.Calendar(firstweekday=5)
pprint.pprint(caldr.monthdatescalendar(2025, 1))

print('#' * 80)
pprint.pprint(caldr.yeardayscalendar(2025), depth=3)
print('#' * 80)
pprint.pprint(caldr.yeardatescalendar(2025, width=5), depth=5)
print('#' * 80)
pprint.pprint(caldr.monthdays2calendar(2025,1))
print('#' * 80)
pprint.pprint(caldr.monthdatescalendar(2025,1))

# CONSOLE
# python - m calendar 2025 1



