#! python
# coding=utf-8
# ********************************************************
# L_002_044_2.py
# 002.Работа с Информационными Файлами
# 044.Работа с JSON Файлами
# --------------------------------------------------------
# Практический Курс по Продвинутому Python (2023)
# https://www.udemy.com/course/avecoder-advanced-python/
# Ave Coder, 2023
# ********************************************************
# Writing by sgiman, May 2025

import json

#=========================================================
# PYTHON TO JSON
#=========================================================
def main():

    # JSON OBJECT
    python_data = {
        "make" : "Opel",
        "model" : "Mokka",
        "colours" : [
            "Black",
            "White",
            "Blue"
        ],
        "price" : 20000.99
    }

    json_str = json.dumps(python_data, indent=3)
    print(json_str)


if __name__ == "__main__":
    main()
