#! python
# coding=utf-8
# ********************************************************
# L_003_001.py
# 003_Случайные числа, Секреты, Пароли и UUID
# 001.Работа со Случайными Числами
# --------------------------------------------------------
# Практический Курс по Продвинутому Python (2023)
# https://www.udemy.com/course/avecoder-advanced-python/
# Ave Coder, 2023
# ********************************************************
# Writing by sgiman, May 2025

import random

print('-' * 80)

# print(random.random())
# print(random.random())
# print(random.random())

# Monet game
# for i in range(10):
#     if random.random() <= 0.5:
#         print("Heads")
#     else:
#         print("Tails")

# 1...100
print(random.uniform(1,100))

print(random.randint(1, 100))

print(random.randrange(0, 101, 5))  # 0...101 with STEP=5

# Идентично при seed=1
print('-' * 80)
random.seed(1)
print(random.random())
print(random.random())

print('-' * 80)
random.seed(1)
print(random.random())
print(random.random())

print('-' * 80)


