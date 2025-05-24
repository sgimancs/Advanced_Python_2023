#! python
# coding=utf-8
# ********************************************************
# L_001_046.py
# 001.Разогрев
# 046.Docstrings (Строки Документации)
# --------------------------------------------------------
# Практический Курс по Продвинутому Python (2023)
# https://www.udemy.com/course/avecoder-advanced-python/
# Ave Coder, 2023
# ********************************************************
# Writing by sgiman, May 2025

# HELP (DOCS)
# print(map.__doc__)      # help for "map"

def my_function(arg1, arg2):
    """
    -----------------------------------------------------
    my_function(arg1, arg2=None) --> no purpose function

    Parameters:
        arg1: first argument, any type
        arg2: second argument, defaults to None
    -----------------------------------------------------
    """
    print(arg1, arg2)


def main():
    print(my_function.__doc__)


if __name__=="__main__":
    main()
