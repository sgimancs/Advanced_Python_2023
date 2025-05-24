#! python
# coding=utf-8
# ********************************************************
# L_004_041.py
# 004.Дата и Время
# 041.Таймеры (Замеряем Время Выполнения Кода)
# --------------------------------------------------------
# Практический Курс по Продвинутому Python (2023)
# https://www.udemy.com/course/avecoder-advanced-python/
# Ave Coder, 2023
# ********************************************************
# Writing by sgiman, May 2025

import time

def main():
    start = time.perf_counter()     # таймер с точкой отчёта

    a_list = [1, 2, 3, 4, 5]
    b_list = [6, 7, 8, 9, 10]
    c_list = []                     # результат операций над списками

    for a, b in zip(a_list, b_list):
        c_list.append(a * b)

    print(c_list)

    time.sleep(4)                   # задержка на 4 сек.

    finish = time.perf_counter()    # текущее время после выполнения

    print(f'Execution time: {finish - start:0.4f} seconds')


#=========================
# START
#=========================
if __name__ == '__main__':
    main()


