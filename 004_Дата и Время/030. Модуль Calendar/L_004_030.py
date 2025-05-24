#! python
# coding=utf-8
# ********************************************************
# L_004_030.py
# 004.Дата и Время
# 030.Модуль Calendar
# --------------------------------------------------------
# Практический Курс по Продвинутому Python (2023)
# https://www.udemy.com/course/avecoder-advanced-python/
# Ave Coder, 2023
# ********************************************************
# Writing by sgiman, May 2025

import calendar


cal = calendar.month(2025, 1)
print('-' * 80)
print(cal)          # календарь
print(type(cal))    # <class 'str'>

#-----------------------------------------------------------
print('-' * 80)
#cal = calendar.month(2025, 1, w=5, l=5)
cal_mnth = calendar.prmonth(2025, 1)
print(cal)

#-----------------------------------------------------------
print('-' * 80)
cal_out = calendar.calendar(2025, c=5, m=2)     # c-отступы, m-месяцы
print(cal_out)

#-----------------------------------------------------------
print('-' * 80)
calendar.setfirstweekday(calendar.SATURDAY)
print(calendar.month(2025,1))

#-----------------------------------------------------------
print('-' * 80)
ltc_ru = calendar.LocaleTextCalendar(locale='ru_RU')
print(ltc_ru.formatmonth(2025, 1))

#===========================================================
#  HTML CALENDAR
#===========================================================
print('-' * 80)
html_cal = calendar.HTMLCalendar()
print(html_cal.formatmonth(2025, 1))
#print(html_cal.formatyear(2023, width=5))

#-----------------------------------------------------------
print('-' * 80)
html_cal.cssclasses = ['manic_monday', 'ruby_tuesday',
                       'wednesday_adams', 'black_thursday', 'good_friday',
                       'saturday', 'sunday_bloody_sanday']

print(html_cal.cssclasses)

#-----------------------------------------------------------
print('-' * 80)
html_cal_day = calendar.HTMLCalendar(firstweekday=5)
print(html_cal_day.formatmonth(2025, 1))

#########################
### Calendar as lists ###
