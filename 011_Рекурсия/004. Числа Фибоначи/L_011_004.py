#! python
# coding=utf-8
# **************************************************************
# L_011_004.py
# 011_Рекурсия
# 004.Числа Фибоначчи
# --------------------------------------------------------------
# Практический Курс по Продвинутому Python (2023)
# https://www.udemy.com/course/avecoder-advanced-python/
# Ave Coder, 2023
# **************************************************************
# Writing by sgiman, May 2025

# --------------------------------------------------------------
# Золотое сечение 1.61803399887 - (a+b)/a = 1.6117803
# Кривая Фибоначчи
# Ветви дерева
# Древовидный поиск (метод поиска Фибоначчи в отсортированных массивах)
# Эффективная сортировка и сжатие данных
# Архитектура (пропорции)
# Фото и картины (равновесие и гармония)
# Технический анализ финансовых рынков для прогнозирования
# Музыка (ритм и мелодия)
# Биология (модели роста живых организмов - схемы ветвления сосудов итп)
# Игры (головоломки)
# --------------------------------------------------------------
# f(1) = 1
# f(2) = 1
# f(n) = f(n-1) + f(n-2) если n > 2
# 0, 1, 1, 2, 3, 5, 8 , 13, 21, ...
# --------------------------------------------------------------

def fib(n):
    print(f'Считаю {n} число Фибоначчи')
    if n < 2:
        return 1
    return fib(n - 2) + fib(n - 1)


print('=' * 80)
fib(6)
