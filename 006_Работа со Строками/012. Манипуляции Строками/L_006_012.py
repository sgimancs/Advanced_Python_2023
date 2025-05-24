#! python
# coding=utf-8
# **************************************************************
# L_006_012.py
# 006_Работа со Строками
# 012.Манипуляции Строками
# --------------------------------------------------------------
# Практический Курс по Продвинутому Python (2023)
# https://www.udemy.com/course/avecoder-advanced-python/
# Ave Coder, 2023
# **************************************************************
# Writing by sgiman, May 2025

import string

print('-' * 80)

# "Бетти Боттер купила немного масла"
sample_str2 = 'Betty Botter bought a bit of butter'

# РЕГИСТР (UPPER/LOWER)
print(sample_str2.upper())  # верхний регистр
print(sample_str2.lower())  # нижний регистр

# РАЗДЕЛЕННИЕ (SPLIT)
print('-' * 80)
split_res = sample_str2.split(" ")  # список (разделение по пробелу)
print(split_res)

# СОЕДИНЕНИЕ (JOIN)
print('-' * 80)
join_res = ", ".join(split_res)     # cоединение с запятыми
print(join_res)
join_res = " ".join(split_res)      # cоединение с пробелами
print(join_res)
