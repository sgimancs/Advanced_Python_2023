#! python
# coding=utf-8
# **************************************************************
# L_007_036.py
# 007.Итераторы и Генераторы
# 036.Лямбда
# --------------------------------------------------------------
# Практический Курс по Продвинутому Python (2023)
# https://www.udemy.com/course/avecoder-advanced-python/
# Ave Coder, 2023
# **************************************************************
# Writing by sgiman, May 2025

# FUNC
def func(x): return x+x

# LAMBDA
lambda x: x + x

###############################################################
# ARGUMENT
print('#' * 80)
print((lambda x: x*2)(14))

# LIST
list_1 = [1,2,3,4,5,6,7,8,9]

# Удвоение списка
list_obj = (lambda x: x*2)
print('#' * 80)
print(list_obj(list_1))

list_2 = []
for x in list_1:
    temp = lambda x: x*2
    list_2.append(temp(x))

print('#' * 80)
print(list(list_2))

###############################################################
# STRINGS
str1 = 'Sgiman'
rev_upper = lambda x: x.upper()[::-1]   # c переворотом
print(rev_upper(str1))

###############################################################
# LIST COMPREHENSIONS
print('#' * 80)
is_even_list = [lambda arg=x: arg * 10 for x in range(1, 15)]
for item in is_even_list:
    print(item())

###############################################################
# IF-ELSE
print('#' * 80)
cond = lambda a,b : a if (a > b) else b
print(cond(10, 20))

###############################################################
print('#' * 80)
mult_list = [[12, 23, 56], [2, 6, 14, 72], [13, 5, 7, 22]]  # список списков
print(mult_list)

srt_lst = lambda x: (sorted(i) for i in x)              # сортировка по возрастанию (внутри списков)
sec_lrg = lambda x, f : [y[len(y)-2] for y in f(x)]     # вторые по величине
res = sec_lrg(mult_list, srt_lst)
print(res)


