#! python
# coding=utf-8
# **************************************************************
# L_011_011.py
# 011_Рекурсия
# 006.Числа Фибоначчи (Знакомство с Мемоизацией)
# --------------------------------------------------------------
# Практический Курс по Продвинутому Python (2023)
# https://www.udemy.com/course/avecoder-advanced-python/
# Ave Coder, 2023
# **************************************************************
# Writing by sgiman, May 2025


### native iteration
# raise. Возбуждает указанное исключение
def fibonacci_inter(n):
    if n < 0:
        raise ValueError("n must be > 0")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a = 0
        b = 1
        for i in range(n-1):
            c = a + b
            a = b   # текущее значение
            b = c   # n-e значение в ряду Фибоначчи (итерация)
        return b

### recursive
def fibonacci_rec(n):
    if n < 0:
        raise ValueError("n must be > 0")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_rec(n-1) + fibonacci_rec(n-2)  # двойной вызов (рекурсия)


#*************************
#  START
#*************************
if __name__ == '__main__':
    print('=' * 80)
    print("iterative: ", fibonacci_inter(9))
    print('=' * 80)
    print("iterative: ", fibonacci_rec(9))
