#! python
# coding=utf-8
# **************************************************************
# L_007_089.py
# 007.Итераторы и Генераторы
# 089.Генераторы Продвинутые Методы
# --------------------------------------------------------------
# Практический Курс по Продвинутому Python (2023)
# https://www.udemy.com/course/avecoder-advanced-python/
# Ave Coder, 2023
# **************************************************************
# Writing by sgiman, May 2025

print('=' * 80)

# Числовые палиндромы (перевёрнутые числа)
def is_palindrom(num):
    if num // 10 == 0:
        return False
    temp = num
    reversed_num = 0

    while temp != 0:
        reversed_num = (reversed_num * 10) + (temp % 10)
        temp = temp // 10

    if num == reversed_num:
        return True
    else:
        return False


#################################################################

def infinity_palindromes():
    num = 0
    while True:
        if is_palindrom(num):
            i = (yield num)
            if i is not None:
                num = i
        num += 1


if __name__ == '__main__':
    #print(is_palindrom(1001))
    pal_gen = infinity_palindromes()

    for i in pal_gen:
        digits = len(str(i))

        # Исключение (error)
        if digits == 10:
            # pal_gen.throw(ValueError('Too Long'))
            pal_gen.close() # Stop
        # Послать значение обратно в генератор: infinity_palindromes()
        pal_gen.send(10 ** (digits))
        print(i)
