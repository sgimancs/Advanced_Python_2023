#! python
# coding=utf-8
# ********************************************************
# L_004_023.py
# 004.Дата и Время
# 023.Вычисление Временной Разницы (Интервала)
# --------------------------------------------------------
# Практический Курс по Продвинутому Python (2023)
# https://www.udemy.com/course/avecoder-advanced-python/
# Ave Coder, 2023
# ********************************************************
# Writing by sgiman, May 2025

from datetime import date, time, datetime, timedelta

dt1 = datetime(2022, 6, 1, 12)
dt2 = datetime(2022, 1, 6, 12)

print('-' * 80)
print(dt1>dt2)      # True
print(dt1<dt2)      # False

delta = dt1 - dt2
print(delta)
print('DAYS: ', delta.days)
print('SEC: ', delta.seconds)

print('-' * 80)

#====================================#
# Расчёт завершения для подписки
#====================================#
now = datetime.now()
one_month = timedelta(days=30)
one_week = timedelta(weeks=1)

print("One month+ :", now + one_month)
print("One week+ :", now + one_week)
print("One week- :", now - one_week)
print('-' * 80)