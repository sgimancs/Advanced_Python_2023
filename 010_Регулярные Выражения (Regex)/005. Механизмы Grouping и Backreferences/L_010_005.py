#! python
# coding=utf-8
# **************************************************************
# L_009_005.py
# 010.Регулярные Выражения (Regex)
# 005.Механизмы Grouping и Backreferences
# --------------------------------------------------------------
# Практический Курс по Продвинутому Python (2023)
# https://www.udemy.com/course/avecoder-advanced-python/
# Ave Coder, 2023
# **************************************************************
# Writing by sgiman, May 2025

import re

###### ()

print('=' * 80)
print(re.search('(coder)', 'ave coder moder'))
print(re.search('coder', 'ave coder moder'))

print('-' * 80)
print(re.search('coder+', 'ave coder moder'))
print(re.search('coder+', 'ave coderrr moder'))

print('-' * 80)
print(re.search('(coder)+', 'ave coder moder'))
print(re.search('(coder)+', 'ave codercoder moder'))
print(re.search('(coder)+', 'ave codercodercoder moder'))

print('-' * 80)
print(re.search('([cm]oder){1,5}(noder)?', 'ave codermodernoder'))
print(re.search('([cm]oder){1,5}(noder)?', 'ave codermoder'))
print(re.search('([cm]oder){1,5}(noder)?', 'ave moder'))
print(re.search('([cm]oder){1,5}(noder)?', 'modernoder'))

print('-' * 80)
print(re.search(r'(ave(coder)?)+(\d\d\d)?', 'avecoder123'))
print(re.search(r'(ave(coder)?)+(\d\d\d)?', 'avemaria'))
print(re.search(r'(ave(coder)?)+(\d\d\d)?', 'avemaria123'))
print(re.search(r'(ave(coder)?)+(\d\d\d)?', 'ave123'))

#######################################################################
print('=' * 80)

m = re.search(r'(\w+),(\w+),(\w+)', 'ave,coder,moder')
print(m.group())        # ave,coder,moder
print(m.group(1))       # ave
print(m.group(2))       # coder
print(m.group(3))       # moder
print(m.group(0))       # ave,coder,moder
print(m.group(1,2))     # ('ave', 'coder')

print(len(m.groups()))  # 3
print(len(m.group()))   # 15

###### BACKREFERENCES ######
# Обратные ссылки

print('=' * 80)

pattern = r'(\w+),\1'

m = re.search(pattern, "ave,ave")
print(m)

m = re.search(pattern, 'coder,coder')
print(m)

###### (?P<name><regex>)
print('=' * 80)

m = re.search(r'(?P<name1>\w+),(?P<name2>\w+),(?P<name3>\w+)', 'ave,coder,moder')
print(m.groups())
print(m.group(1))
print(m.group('name1'))

###### (?P<name>)
print('=' * 80)

pattern = r'(\w+),\1'
m = re.search(pattern, 'ave,ave')
print(m)

# m = re.search(r'(?P<salutation>\w+), (?P=salutation)', 'ave,ave')
# print(m)
# print(m.group('salutation'))


