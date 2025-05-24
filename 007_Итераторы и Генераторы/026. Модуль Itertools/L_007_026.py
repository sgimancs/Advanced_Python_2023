#! python
# coding=utf-8
# **************************************************************
# L_007_026.py
# 007.Итераторы и Генераторы
# 026.Модуль Itertools
# --------------------------------------------------------------
# Практический Курс по Продвинутому Python (2023)
# https://www.udemy.com/course/avecoder-advanced-python/
# Ave Coder, 2023
# **************************************************************
# Writing by sgiman, May 2025

import itertools

def main() :
    print('#' * 80)
    #days_ua = ["Понеділок", "Вівторок", "Середа", "Четвер", "П'ятниця", "Субота", "Неділя"]
    dni = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Субота", "Воскресенье"]
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    cycle_days = itertools.cycle(days)
    print(next(cycle_days))
    print(next(cycle_days))
    print(next(cycle_days))
    print(next(cycle_days))
    print(next(cycle_days))
    print(next(cycle_days))
    print(next(cycle_days))

    ############################################################
    print('#' * 80)
    count_stuff = itertools.count(100, 10)  # start, step
    print(next(count_stuff))
    print(next(count_stuff))
    print(next(count_stuff))
    print(next(count_stuff))
    print(next(count_stuff))

    ############################################################
    print('#' * 80)
    prices = [10, 20, 30, 40, 50, 40, 30, 20, 10, 100]
    acc = itertools.accumulate(prices, max)
    print(list(acc))
    acc = itertools.accumulate(prices, min)
    print(list(acc))

    ############################################################
    print('#' * 80)
    chain_stuff = itertools.chain(days, prices)
    print(list(chain_stuff))

    ############################################################
    def test_func(x):
        return x < 50

    print('#' * 80)
    print(list(itertools.dropwhile(test_func, prices)))     # игнорировать начало до 50
    print(list(itertools.takewhile(test_func, prices)))     # игнорировать конец до 50

if __name__ == "__main__":
    main()

