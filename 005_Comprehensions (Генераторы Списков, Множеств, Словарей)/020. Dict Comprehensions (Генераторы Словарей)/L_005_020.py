#! python
# coding=utf-8
# **************************************************************
# L_005_020.py
# 005.Comprehensions (Генераторы Списков, Множеств, Словарей)
# 020.Dict Comprehensions (Генераторы Словарей)
# --------------------------------------------------------------
# Практический Курс по Продвинутому Python (2023)
# https://www.udemy.com/course/avecoder-advanced-python/
# Ave Coder, 2023
# **************************************************************
# Writing by sgiman, May 2025

# Comprehensions - Понимание

def main():
    print('-' * 80)

    # --------------------
    #  Температура
    # --------------------
    ctemps = [0, 10, 44, 100, 120]  # список
    temp_dict = {t: (t * 9/5) + 32 for t in ctemps if t < 100}  # градусы в фаренгейт
    print(temp_dict)
    print(temp_dict[10])    # вывести по ключу 10
    print('-' * 80)

    # ------------------------------
    #  СЛОВАРИ ИГРОКОВ С НОМЕРАМИ
    # ------------------------------
    team1 = {"Adams": 14, "Pears": 28, "Hendrics": 44, "Ericsson": 1}
    team2  = {"Parquette": 16, "Duvall": 67, "Lafleur" : 5}

    new_team = {k: v for team in (team1, team2) for k, v in team.items()}   # объединить два словаря
    print(new_team)

    tm = {**team1, **team2} # Соединяем словари в переменную tm
    print(tm)

    print('-' * 80)


if __name__ == "__main__":
    main()

