#! python
# coding=utf-8
# **************************************************************
# L_008_001_2.py
# 008.Манипулирование Данными
# 001.Сортировка Данных (Функция sorted())
# --------------------------------------------------------------
# Практический Курс по Продвинутому Python (2023)
# https://www.udemy.com/course/avecoder-advanced-python/
# Ave Coder, 2023
# **************************************************************
# Writing by sgiman, May 2025

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

# SORT & PRICE
def sort_products(product):
    return product.price

##########################################################################
print('=' * 80)
print(sorted(product_list, key=sort_products))      # cортировка по price (sort_products())
print(sorted(product_list, key=lambda p:p.price))   # cортировка по price (lambda)
print(sorted(product_list, key=lambda p:p.discount_price()))    # цена со скидкой

##########################################################################
print('=' * 80)
print('SORT PRICE:', sorted(product_list, key=lambda p:p.price))  # сортировка по цене
print('SORT WEIGHT:', sorted(product_list, key=lambda p:p.weight))  # сортировка по весу

# Cортировка по цене и весу (???)
# print('=' * 80)
# print(sorted(product_list, key=lambda p:p.price))       # sort price
# result = (sorted(product_list, key=lambda p:p.weight))  # sort wight
# print(sorted(result))
