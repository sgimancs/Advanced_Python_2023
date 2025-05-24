#! python
# coding=utf-8
# ********************************************************
# L_002_044.py
# 002.Работа с Информационными Файлами
# 044.Работа с JSON Файлами
# --------------------------------------------------------
# Практический Курс по Продвинутому Python (2023)
# https://www.udemy.com/course/avecoder-advanced-python/
# Ave Coder, 2023
# ********************************************************
# Writing by sgiman, May 2025

import json
from json import JSONDecodeError


#=========================================================
# FROM JSON TO PYTHON
#=========================================================
def main():

    # JSON STRING
    json_str = ''' {
        "make" : "Opel",
        "model" : "Mokka",
        "colours" : [
            "Black",
            "White",
            "Blue"
        ],
        "price" : 20000.99
    }'''

    print('-' * 80)
    try:
        data = json.loads(json_str)     # создать json объект (словарь)
        print("SUCCESSFULLY!")
    except JSONDecodeError as err:
        print("JSON Decoding Error: ")
        print(err.msg)                      # сообщение
        print(err.linenom, err.colno)       # номер столбца



    print('-' * 80)
    print("Car: " + data['make'])
    if (data['model'] == 'Mokka'):
        print("It\'s Mokka!")

    print('-' * 80)
    for colour in data['colours']:
        print('Colours: ' + colour)


if __name__ == "__main__":
    main()
