#! python
# coding=utf-8
# **************************************************************
# L_024_001.py
# 006_Работа со Строками
# 024.Форматирование Строк
# --------------------------------------------------------------
# Практический Курс по Продвинутому Python (2023)
# https://www.udemy.com/course/avecoder-advanced-python/
# Ave Coder, 2023
# **************************************************************
# Writing by sgiman, May 2025

import string
#from string import Template

# $animal, $action
# "Быстрое коричневое $животное $действие над ленивой собакой"
the_str = "The quick brown $animal $action over the lazy dog"
the_template = string.Template(the_str)
output_str = the_template.substitute(animal='fox', action='jumped')

print('=' * 80)
print(output_str)

############################################################################
# СЛОВАРИ
print('=' * 80)
args = {
    "animal": "cow",    # корова
    "action": "ran"     # cбежала
}

output_str = the_template.substitute(args)
print(output_str)   # "Быстрая коричневая корова переехала ленивую собаку"

############################################################################
# F-СТРОКИ
print('=' * 80)
product = "laptop"  # товар
price = "199.99"    # цена
tax = 0.08          # налог
print(f"{product} has a price of {price}, plus {tax} tax")


