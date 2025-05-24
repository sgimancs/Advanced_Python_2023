#! python
# coding=utf-8
# ********************************************************
# L_003_012.py
# 003_Случайные числа, Секреты, Пароли и UUID
# 012.Операции с Последовательностями Случайных Чисел
# --------------------------------------------------------
# Практический Курс по Продвинутому Python (2023)
# https://www.udemy.com/course/avecoder-advanced-python/
# Ave Coder, 2023
# ********************************************************
# Writing by sgiman, May 2025

import random
import string

print('-' * 80)
traffic_lights = ["Red", "Yellow", "Green"]
timing = [30, 2, 15]                                        # веса предпочтений

# Выборка с замещением
#print(random.choice(traffic_lights, timing, k=10))         # k - кол-во случайных элементов - ????

# Выборка без замещения (simple)
random_letters = random.sample(string.ascii_lowercase, 10)
print(random_letters)
print('-' * 80)

# Перемешать список (shuffle)
players = ["joan", "Jane", "Jenny", "Jenifer", "Joceline"]
random.shuffle(players)
print(players)
print('-' * 80)


#===================================================================#



