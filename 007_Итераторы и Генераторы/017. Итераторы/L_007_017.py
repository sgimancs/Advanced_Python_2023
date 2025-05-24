#! python
# coding=utf-8
# **************************************************************
# L_007_017.py
# 007.Итераторы и Генераторы
# 017.Итераторы
# --------------------------------------------------------------
# Практический Курс по Продвинутому Python (2023)
# https://www.udemy.com/course/avecoder-advanced-python/
# Ave Coder, 2023
# **************************************************************
# Writing by sgiman, May 2025

def main() :

    print('#' * 80)
    #days_ua = ["Понеділок", "Вівторок", "Середа", "Четвер", "П'ятниця", "Субота", "Неділя"]
    dni = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Субота", "Воскресенье"]
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # Итерация списка
    i = iter(days)
    print(next(i))
    print(next(i))
    print(next(i))
    print(next(i))

    #############################################################
    print('#' * 80)
    # fp - file pointer, sentinel = '' (часовой)
    with open('../026. Модуль Itertools/textfile.txt', "r") as fp:
        for line in iter(fp.readline, ''):
            print(line)


if __name__ == "__main__":
    main()

