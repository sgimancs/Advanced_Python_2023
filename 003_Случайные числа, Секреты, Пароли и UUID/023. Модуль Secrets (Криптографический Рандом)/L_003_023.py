#! python
# coding=utf-8
# ********************************************************
# L_003_023.py
# 003_Случайные числа, Секреты, Пароли и UUID
# 023.Модуль Secrets (Криптографический Рандом)
# --------------------------------------------------------
# Практический Курс по Продвинутому Python (2023)
# https://www.udemy.com/course/avecoder-advanced-python/
# Ave Coder, 2023
# ********************************************************
# Writing by sgiman, May 2025

import os
import secrets

# Random HEX
print('-' * 80)
results = os.urandom(10)
print([hex(b) for b in results])
print('-' * 80)

# Случайный криптографический выбор
traffic_lights = ["red", "Yellow", "Green"]
print(secrets.choice(traffic_lights))
print('-' * 80)

# Случайные токены
byte_results = secrets.token_bytes(8)   # bytes
print(byte_results)
print('-' * 80)

hex_results = secrets.token_hex(8)      # hex
print(hex_results)
print('-' * 80)

# url_results = secrets.token_urlsafe(8)  # word
url_results = secrets.token_urlsafe()  # word
print(url_results)
print('-' * 80)
