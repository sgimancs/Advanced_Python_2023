#! python
# coding=utf-8
# **************************************************************
# L_011_002.py
# 011_Рекурсия
# 002.Факториал
# --------------------------------------------------------------
# Практический Курс по Продвинутому Python (2023)
# https://www.udemy.com/course/avecoder-advanced-python/
# Ave Coder, 2023
# **************************************************************
# Writing by sgiman, May 2025

# n! = 1 * 2 * 3 *...
# !0 = 1
# !1 = 1
# n! = 1 * 2 * … * n,
# n! = 1 * … * (n-2) * (n-1) * n,

###### Variant 1 ######
print('=' * 80)

n = int(input('Введите целое положительное число (вариант 1): '))

factorial = 1
while n > 1:
    factorial *= n
    n -= 1

print(factorial)


###### Variant 2 (цикл) ######
print('=' * 80)
n = int(input('Введите целое положительное число (вариант 2): '))
factorial = 1

for i in range(2, n+1):
    factorial *= i

print(factorial)
