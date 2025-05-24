#! python
# coding=utf-8
# **************************************************************
# L_009_002.py
# 009.Логирование
# 002.Базовое Логирование
# --------------------------------------------------------------
# Практический Курс по Продвинутому Python (2023)
# https://www.udemy.com/course/avecoder-advanced-python/
# Ave Coder, 2023
# **************************************************************
# Writing by sgiman, May 2025

import logging

def main():

    logging.basicConfig(level=logging.DEBUG,
                        filename="log_output.log", filemode="w") # с переписыванием лога по новой

    logging.debug("Here's a debug-level log message")       # -
    logging.info("Here's a info-level log message")         # -
    logging.warning("Here's a warning-level log message")   # + (default)
    logging.error("Here's a error-level log message")       # + (default)
    logging.critical("Here's a critical-level log message") # + (default)

    logging.warning("Here's a variable of type {} and int: {}".format("String", 42))

if __name__=="__main__":
    main()

