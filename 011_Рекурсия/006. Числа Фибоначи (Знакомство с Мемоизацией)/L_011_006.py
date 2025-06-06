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

# Мемоизация - это способ запоминания результатов функции,
# чтобы избежать повторного вычисления тех же самых значений.

cache = {0: 0, 1: 1}

def fibonacci_mem(num):
    # base case (если кеш не пустой)
    if num in cache:
        return cache[num]
    # cache fib bum (вычисление числа Фибоначчи)
    cache[num] = fibonacci_mem(num - 1) + fibonacci_mem(num - 2)    # двойной вызов (рекурсия)
    return cache[num]   # вернуть результат в кеш-словаре


#*************************
#  START
#*************************
if __name__ == "__main__":
    print('=' * 80)
    print([fibonacci_mem(num) for num in range(12)])

