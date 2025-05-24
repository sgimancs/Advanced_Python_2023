#! python
# coding=utf-8
# ********************************************************
# L_004_050.py
# 004.Дата и Время
# 050.cProfile
# --------------------------------------------------------
# Практический Курс по Продвинутому Python (2023)
# https://www.udemy.com/course/avecoder-advanced-python/
# Ave Coder, 2023
# ********************************************************
# Writing by sgiman, May 2025

#---------------------------------------------------------
# С-ПРОФИЛИРОВАНИЕ КОДА
# ncalls    - кол-во вызовов
# tottime   - общее время
# percall   - среднее время на вызов
# cumtime   - совокупное время
# precall   - коэффициент (без вызовов рекурсии)
#---------------------------------------------------------

import cProfile, pstats

print('-' * 80)
cProfile.run('20 * 110')

#========================================================
def create_array():
    arr=[]
    for i in range(0, 500000):
        arr.append(i)


def print_statement():
    print('Array created successfully')


def main():
    create_array()
    print_statement()


#============================
# START
#============================
if __name__ == '__main__':
    print('-' * 80)
    #cProfile.run('main()')          # профайлер для main()
    profiler = cProfile.Profile()
    profiler.enable()               # разрешить сбор данных

    main()
    profiler.disable()              # завершить сбор данных
    #stats = pstats.Stats(profiler).sort_stats('ncalls')     # статистика
    stats = pstats.Stats(profiler).sort_stats('cumtime')     # статистика
    print('-' * 80)

    profiler.dump_stats('dump-stats')   # сохранить статистику на HDD

    # Загрузить статистику с HDD
    p = pstats.Stats('dump-stats')
    p.strip_dirs().print_stats()
    print('-' * 80)
