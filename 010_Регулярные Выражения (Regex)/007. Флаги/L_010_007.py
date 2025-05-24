#! python
# coding=utf-8
# **************************************************************
# L_009_007.py
# 010.Регулярные Выражения (Regex)
# 007.Флаги
# --------------------------------------------------------------
# Практический Курс по Продвинутому Python (2023)
# https://www.udemy.com/course/avecoder-advanced-python/
# Ave Coder, 2023
# **************************************************************
# Writing by sgiman, May 2025

import re

### re.I ### re.IGNORECASE
print('=' * 80)
print(re.search('x+', 'xxxXXX'))    # поиск прописных
print(re.search('X+', 'xxxXXX'))    # поиск заглавных

# ИГНОРИРОВАТЬ РЕГИСТР
print('=' * 80)
print(re.search('x+', 'xxxXXX', re.I))
print(re.search('X+', 'xxxXXX', re.IGNORECASE))

print(re.search('[a-z]+', 'aVeCodeR', re.I))
print(re.search('[a-z]+', 'aVeCodeR', re.IGNORECASE))

### re.M ### re.MULTILINE
print('=' * 80)

s = 'ave\ncoder\nmoder'
print(s)

# ^ - начало строки
print(re.search('^ave', s))     # +
print(re.search('^coder', s))   # -
print(re.search('^moder', s))   # -

# $ - конец строки
print(re.search('ave$', s))     # -
print(re.search('coder$', s))   # -

# MULTILINE
print('-' * 80)
print(re.search('^ave', s, re.MULTILINE))
print(re.search('^coder', s, re.MULTILINE))
print(re.search('^moder', s, re.MULTILINE))

print('-' * 80)
print(re.search('ave$', s, re.MULTILINE))
print(re.search('coder$', s, re.MULTILINE))

### re.S ### re.DOTALL
# "точка" - любой символ
print('=' * 80)

print(re.search('ave.coder', 'ave\ncoder'))             # -
print(re.search('ave.coder', 'ave\ncoder', re.DOTALL))  # + (разрешить "точку")
print(re.search('ave.coder', 'ave\ncoder', re.S))       # + analog

### re.X ### re.VERBOSE
print('=' * 80)

# Tel
regex = r'^(\(\d{3}\))?\s*\d{3}[-.]\d{4}$'

print(re.search(regex, '123.4567'))
print(re.search(regex, '123-4567'))
print(re.search(regex, '(890)123-4567'))
print(re.search(regex, '(890) 123-4567'))

print('-' * 80)

regex = r'''^
            (\(\d{3}\))?
            \s*
            \d{3}
            [-.]
            \d{4}
            $
        '''
print(re.search(regex, '123.4567', re.VERBOSE))
print(re.search(regex, '123-4567', re.VERBOSE))
print(re.search(regex, '(890)123-4567', re.VERBOSE))

### re.DEBUG
# print('*' * 80)
# print(re.search('ave.coder', 'aveXcode', re.DEBUG))
#
# print('-' * 80)
# regex = r'^(\(\d{3}\))?\s*\d{3}[-.]\d{4}$'
# print(re.search(regex, '123.4567', re.DEBUG))

### re.A ### re.ASCII
### re.U ### re.UNICODE
### re.L ### re.LOCALE
print('=' * 80)

s = '\u0487\u042E\u0437\u044F'  # кириллица (^Юзя)
print(s)

print(re.search(r'\w+', s))

###########################################################
print('-' * 80)

s = r'sch\u00f6n'
print(s)

print(re.search(r'\w+', s, re.ASCII))
print(re.search(r'\w+', s, re.UNICODE))
print(re.search(r'\w+', s))

###### Combine
print('=' * 80)

print(re.search('^ave', 'AVE\nCODER\nMODER', re.I|re.M))

###### (?<flags)
print('=' * 80)

print(re.search('(?im)^ave', 'AVE\nCODER\nMODER'))
print(re.search('(?s)ave.coder.moder', 'AVE\nCODER\nMODER')) # ??? (?s) - только в начале (-)

###### (?<set_flags>-<remove_flags>:<regex>)
print('=' * 80)

print(re.search('^(?i:ave)coder', 'AVEcoder'))  # +
print(re.search('^(?i:ave)coder', 'AVECODER'))  # -
