#! python
# coding=utf-8
# ********************************************************
# L_004_041_3.py
# 004.Дата и Время
# 041.Таймеры (Замеряем Время Выполнения Кода)
# --------------------------------------------------------
# Практический Курс по Продвинутому Python (2023)
# https://www.udemy.com/course/avecoder-advanced-python/
# Ave Coder, 2023
# ********************************************************
# Writing by sgiman, May 2025

# timeit.timeit(stmt, setup, timer, number)

import timeit


#=========================================================
### TIMEIT ###
print('-' * 80)
print(timeit.timeit('output = 10*5'))

print('-' * 80)
import_module = "import random"
testcode = '''
def test():
    return random.randint(10, 1000)
'''
print(timeit.timeit(stmt=testcode, setup=import_module))
print('-' * 80)

#=========================================================
### DEFAULT TIMER ###
import random

def test():
    return random.randint(10, 1000)

starttime = timeit.default_timer()
print("The start time is :", starttime)
test()
print("The time difference is: ", timeit.default_timer() - starttime)
print('-' * 80)

#=========================================================
### REPEAT ###
import_module = "import random"
testcode = '''
def test():
    return random.randint(10, 100)
'''
print(timeit.repeat(stmt=testcode, setup=import_module, repeat=5))
print('-' * 80)

