#! python
# coding=utf-8
# **************************************************************
# L_007_072.py
# 007.Итераторы и Генераторы
# 082.Генераторы
# --------------------------------------------------------------
# Практический Курс по Продвинутому Python (2023)
# https://www.udemy.com/course/avecoder-advanced-python/
# Ave Coder, 2023
# **************************************************************
# Writing by sgiman, May 2025

# # Бесконечный цикл
# def infinity_sequence():
#     num = 0
#     while True:
#         yield num   # захватывает текущее значение в текущий момент
#         num += 1
#
# print('=' * 80)
# print(infinity_sequence())  # object
#
# # Вывод значений
# for i in infinity_sequence():
#     print(i)

###############################################################
print('=' * 80)

file_name = ('huge_csv.csv')


# Может переполниться память
def csv_reader_test(f):
    fp = open(f)
    result = fp.read().split("\n")
    return result


def csv_reader(file_name):
    for row in open(file_name, "r"):
        yield row   # возврат каждой строки файла


###############################################################
# import cProfile
#
# # C-ПРОФИЛИРОВАНИЕ
# cProfile.run('sum([num ** 2 for num in range(1000000)])')   # генератор генератора (список) - 0.166 seconds
# print('=' * 80)
# cProfile.run('sum((num ** 2 for num in range(1000000)))')   # генератор генератора (кортеж) - 0.478 seconds


###############################################################
# print('=' * 80)

def print_strings():
    yield_str = 'aaaaaaaaaaaaaaaaaaaaaaaa'
    yield yield_str
    yield_str = 'bbbbbbbbbbbbbbbbbbbbbbbb'
    yield yield_str
    yield_str = 'ccccccccccccccccccccccc'
    yield yield_str


iter_print_strings = print_strings()

# ИТЕРАЦИЯ NEXT (для каждого возвращаемого yield)
print(next(iter_print_strings))
print(next(iter_print_strings))
print(next(iter_print_strings))
# print(next(iter_print_strings)) # Исключение: StopIteration (error)

###############################################################
print('=' * 80)

chars = ['a', 'b', 'c', 'd', 'e']

it = iter(chars)

while True:

    try:
        letter = next(it)
    except StopIteration:       # завершить бесконечный цикл
        break

    print(letter)


