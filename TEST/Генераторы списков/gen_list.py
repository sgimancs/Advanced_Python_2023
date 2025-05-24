#! python
# coding=utf-8
#############################################################
# gen_list.py
# Основы Python — кратко. Часть 4. Генераторы списков (2008)
# https://habr.com/ru/articles/30232/
#############################################################
# Writing by sgiman, May 2025

###### Sample 1 ######

print('=' * 80)
res = []
for x in range(1, 25, 2):
    res.append(x)
print(res)


###### Sample 2 ######
# [x for x in range(1, 25, 2)] - console

print('=' * 80)
res = [x for x in range(1, 25, 2)]                      # в одну строку!!!
print(res)
# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]


###### Sample 3 ######

print('=' * 80)
res = [x**2 for x in range(1, 25, 2) if x % 3 != 0]     # c фильтрацией
print(res)
# [1, 25, 49, 121, 169, 289, 361, 529]


###### Sample 4 ######

print('=' * 80)
dic = {'John':1200, 'Paul':1000, 'Jones':1850, 'Dorothy': 950}
print("\n".join(["%s = %d" % (name, salary) for name, salary in dic.items()]))  # c-style

print('=' * 80)
print("\n".join([f"{name} = {salary}" for name, salary in dic.items()]))        # f-string
'''
Jones = 1850
Dorothy = 950
Paul = 1000
John = 1200
'''
