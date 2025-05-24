#! python
# coding=utf-8
# ********************************************************
# L_001_028.py
# 001.Разогрев
# 028.Функция any()
# --------------------------------------------------------
# Практический Курс по Продвинутому Python (2023)
# https://www.udemy.com/course/avecoder-advanced-python/
# Ave Coder, 2023
# ********************************************************
# Writing by sgiman, May 2025

print('-' * 80)

def contains_numbers(var):
    for char in var:
        if char.isdigit():
            return True
    return False

print(contains_numbers('one is done'))
print(contains_numbers('1 is done'))
print('-' * 80)

###### ANY ######
def contains_numbers(var):
    return any(char.isdigit()   # any()
        for char in var
        )

print(contains_numbers('one is done'))
print(contains_numbers('1 is done'))
print('-' * 80)
