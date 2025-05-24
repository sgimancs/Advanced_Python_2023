#! python
# coding=utf-8
# ********************************************************
# L_001_039.py
# 001.Разогрев
# 039.Приятная Печать Данных с функцией pprint()
# --------------------------------------------------------
# Практический Курс по Продвинутому Python (2023)
# https://www.udemy.com/course/avecoder-advanced-python/
# Ave Coder, 2023
# ********************************************************
# Writing by sgiman, May 2025

import pprint

# Список словарей
ave_data = [{'Strings':'One', 'Integer': 10, 'Floats':[4.24, 42.6]},
            {'Strings':'Two', 'Integer': 20, 'Floats':[6.43, 65.2]},
            {'Strings': 'Three', 'Integer': 30, 'Floats': [9.87, 8.87]}]

# Стандартная печать в одну строку
print(ave_data)
print('-' * 80)

# Приятная Печать Данных (pprint.pprint)
pprint.pprint(ave_data)
print('-' * 80)

pprint.pprint(ave_data, width=30)
print('-' * 80)

pprint.pprint(ave_data, depth=2)
print('-' * 80)

pprint.pprint(ave_data, depth=3)
print('-' * 80)

pprint.pprint(ave_data, indent=3, width=3, depth=3)
print('-' * 80)

ave_more_data = [list(range(10)), list(range(100, 120))]
print(ave_more_data)
pprint.pprint(ave_more_data, width=45, compact=True)
print('-' * 80)

# standard
print(ave_data)
print(type(ave_data))
print('-' * 80)

str_ave_data = str(ave_data)
print(str_ave_data)
print(type(str_ave_data))
print('-' * 80)

# pprint.ppformat
pp_ave_data = pprint.pformat(ave_data)
print(pp_ave_data)
print(type(pp_ave_data))
print('-' * 80)

# with options
print(pprint.pformat(ave_data, depth=3, width=50, indent=2))
print('-' * 80)

