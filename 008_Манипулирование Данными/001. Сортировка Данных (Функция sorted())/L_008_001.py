#! python
# coding=utf-8
# **************************************************************
# L_008_001.py
# 008.Манипулирование Данными
# 001.Сортировка Данных (Функция sorted())
# --------------------------------------------------------------
# Практический Курс по Продвинутому Python (2023)
# https://www.udemy.com/course/avecoder-advanced-python/
# Ave Coder, 2023
# **************************************************************
# Writing by sgiman, May 2025


scores = [18, 6, 21, 20, 43, 22, 33, 60, 8, 4, 3, 6, 16, 31, 34]
print('=' * 80)
print(scores)

###### SORTED ######
sorted_scores = sorted(scores)  # по возрастанию
print(sorted_scores)

reverse_sorted_scores = sorted(scores, reverse=True)
print(reverse_sorted_scores)
