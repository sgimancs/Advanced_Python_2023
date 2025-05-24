#! python
# coding=utf-8
# **************************************************************
# L_008_001.py
# 008.Манипулирование Данными
# 001.Сортировка Данных (Функция sorted())
# --------------------------------------------------------------
# Практический Курс по Продвинутому Python (2023)
# https://www.udemy.com/course/avecoder-advanced-python/
# Ave Coder, 2023
# **************************************************************
# Writing by sgiman, May 2025

from operator import attrgetter, methodcaller, itemgetter

#==============================================================
# Product (CLASS)
#==============================================================
class Product:
    # Constructor
    def __init__(self, name, price, weight, discount):
        self.name = name
        self.price = price
        self.weight = weight
        self.discount = discount

    # Override (???) - переопределение репрезентации
    def __repr__(self):
        return repr((self.name, self.price, self.weight))

    # PRICE CORRECT (скидка)
    def discount_price(self):
        return self.price - (self.price * self.discount)


#------------------------------------------------------------------------#
# PRODUCTS LIST (objects for class Product)
product_list = [
    Product("Laptop", 60, 30, 0.5),
    Product("Laptop", 60, 10, 0.5),
    Product("Phone", 100, 40, 0.1),
    Product("Router", 20, 15, 0.25),
    Product("Camera", 75, 80, 0.75),
]

#=======================================================================#
###### Attrgetter ######
print('=' * 80)
print('Attrgetter Methods:')
# Сортировка по весу в реверсе по убыванию
print(sorted(product_list, key=attrgetter("weight"), reverse=True))

#=======================================================================#
###### Methodcaller ######
print('=' * 80)
print('Methodcaller:')
print(sorted(product_list, key=methodcaller("discount_price")))

#=======================================================================#
###### Methodcaller ######
dumbbels = [("dumbbell", 15),
            ("dumbbell", 50),
            ("dumbbell", 20),
            ("dumbbell", 5),
            ("dumbbell", 25),
            ("dumbbell", 10)]

print('=' * 80)
print(sorted(dumbbels, key=itemgetter(1)))

