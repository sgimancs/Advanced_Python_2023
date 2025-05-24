#! python
# coding=utf-8
# **************************************************************
# L_005_010.py
# 005.Comprehensions (Генераторы Списков, Множеств, Словарей)
# 010.Set Comprehensions (Генераторы Множеств)
# --------------------------------------------------------------
# Практический Курс по Продвинутому Python (2023)
# https://www.udemy.com/course/avecoder-advanced-python/
# Ave Coder, 2023
# **************************************************************
# Writing by sgiman, May 2025

# Comprehensions - Понимание

# --------------------------------
#  Список градусов в фаренгейт
# --------------------------------
def main():

    ctemps = [6, 11, 13, 16, 11, 23, 45, 33, 13, 24, 12, 17, 22]

    print('-' * 80)

    far_temps1 = [(t * 9/5) + 32 for t in ctemps]
    far_temps2 = [(t * 9/5) + 32 for t in ctemps]

    print(far_temps1)
    print(far_temps2)

    # --------------------------------
    #  СТРОКИ
    # --------------------------------
    # EN-панграмма
    # "Быстрая бурая лиса перепрыгнула через ленивую собаку"
    print('-' * 80)
    temp_str = "The quick brown fox jumped over the lazy dog"
    # characters = { c.upper() for c in temp_str }    # EN алфавит c пробелом (если литера присутствует в строке)
    characters = {c.upper() for c in temp_str if not c.isspace()}   # без пробела
    print(characters)


# ===========================
#  START
# ===========================
if __name__ == "__main__":
    main()
