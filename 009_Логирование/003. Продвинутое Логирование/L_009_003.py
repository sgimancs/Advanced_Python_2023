#! python
# coding=utf-8
# **************************************************************
# L_009_003.py
# 009.Логирование
# 003.Продвинутое Логирование
# --------------------------------------------------------------
# Практический Курс по Продвинутому Python (2023)
# https://www.udemy.com/course/avecoder-advanced-python/
# Ave Coder, 2023
# **************************************************************
# Writing by sgiman, May 2025

import logging


extra_data = {'user' : 'sman@sgiman.com'}


def debug_log():
    logging.debug("Here.s a debug-level log msg", extra=extra_data)


def main():
    ###### FORMAT (с форматирующими токенами) ######
    datestr = "%m/%d/%Y %I:%M:%S %p"
    fmtstr = "User:%(user)s %(asctime)s: %(levelname)s: %(funcName)s: Line:%(lineno)d %(message)s"

    logging.basicConfig(filename="output.log",
                        level=logging.DEBUG,
                        filemode="w",
                        format=fmtstr,
                        datefmt=datestr)

    logging.info("Here's an info-level log message", extra=extra_data)
    logging.warning("Here's a warning-level log message", extra=extra_data)

    debug_log()

##################################################################


if __name__=="__main__":
    main()
