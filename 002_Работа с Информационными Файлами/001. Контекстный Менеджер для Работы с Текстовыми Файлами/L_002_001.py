#! python
# coding=utf-8
# ********************************************************
# L_002_001.py
# 002.Работа с Информационными Файлами
# 001.Контекстный Менеджер для Работы с Текстовыми Файлами
# --------------------------------------------------------
# Практический Курс по Продвинутому Python (2023)
# https://www.udemy.com/course/avecoder-advanced-python/
# Ave Coder, 2023
# ********************************************************
# Writing by sgiman, May 2025

# import fileinput

# open - write
fp = open("text.txt", "w")
fp.write("test test test\n")
fp.close()

# Контекстный менеджер with...as (c авто close)
with open("text.txt", "r") as fp:   # fp - указатель на открытый файл
    data = fp.read()
    print(data)

# С добавлением в конец файла (чтение-запись)
with open("text.txt", "a+") as fp:
    fp.write("added more tests\n")
    fp.seek(0)                      # в начало
    data = fp.read()
    print(data)







