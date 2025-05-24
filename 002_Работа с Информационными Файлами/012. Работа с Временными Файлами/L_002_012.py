#! python
# coding=utf-8
# ********************************************************
# L_002_012.py
# 002.Работа с Информационными Файлами
# 012.Работа с Временными Файлами
# --------------------------------------------------------
# Практический Курс по Продвинутому Python (2023)
# https://www.udemy.com/course/avecoder-advanced-python/
# Ave Coder, 2023
# ********************************************************
# Writing by sgiman, May 2025

# CTRL+D - копирование строки (pyCharm)

import os
import tempfile

print('-' * 80)

# Help gettempdir()
print('gettempdir()', tempfile.gettempdir())
print('gettempdir()', tempfile.gettempprefix())

print('-' * 80)

#----------------------------------
# VARIANT 1
#----------------------------------
(tempfh, tempfp) = tempfile.mkstemp(".tmp", "test_tmp", None, True)
f = os.fdopen(tempfh, "w+t")    # низко-уровневая в стиле С++
f.write('Temp text data')   # записать
f.seek(0)                   # в начало
print(f.read())             # читать
f.close()                   # закрыть
os.remove(tempfp)           # удалить

print('-' * 80)

#----------------------------------
# VARIANT 2
#----------------------------------
with tempfile.TemporaryFile(mode='w+t') as tfp:
    tfp.write('Some more temp text data')
    tfp.seek(0)
    print(tfp.read())

print('-' * 80)

#----------------------------------
# VARIANT 3 (???)
#----------------------------------
# with tempfile.TemporaryDirectory() as tdp:
#     path = os.path.join(tdp, "tmp_txt.txt")
#     print(path)
#     tfp = open(path, "w+t")
#     tfp.write("The next temp text data")
#     tfp.seek(0)
#     print(tfp.read())

