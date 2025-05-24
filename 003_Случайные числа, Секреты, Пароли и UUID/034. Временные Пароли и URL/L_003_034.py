#! python
# coding=utf-8
# ********************************************************
# L_003_034.py
# 003_Случайные числа, Секреты, Пароли и UUID
# 034.Временные Пароли и URL
# --------------------------------------------------------
# Практический Курс по Продвинутому Python (2023)
# https://www.udemy.com/course/avecoder-advanced-python/
# Ave Coder, 2023
# ********************************************************
# Writing by sgiman, May 2025

import secrets
import string

from pandas.core.computation.common import result_type_many


#---------------------------------------------------------
# Временные пароли (variant 1)
#---------------------------------------------------------
def generate_temp_password(number_of_characters=8):
    char_pool = string.ascii_letters + string.digits + "+-?/!@#$%^"
    result = ''.join(secrets.choice(char_pool) for i in range(number_of_characters))
    return result


print('-' * 80)
print(generate_temp_password(10))
print('-' * 80)

#---------------------------------------------------------
# Временные пароли (variant 2)
#---------------------------------------------------------
def generate_perm_password(number_of_characters=8):
    char_pool = string.ascii_letters + string.digits + "+-?/!@#$%^"
    while True:
        result = ''.join(secrets.choice(char_pool) for i in range(number_of_characters))
        if any(c.isupper() for c in result) and any(c.isdigit() for c in result):
            break

    return result


print(generate_perm_password(10))
print('-' * 80)

#---------------------------------------------------------
# ЗАКОДИРОВАННЫЙ URL (для сброса пароля)
#---------------------------------------------------------
result_url = "http://www.example.com?reset="
result_url += secrets.token_urlsafe(15)
print(result_url)
