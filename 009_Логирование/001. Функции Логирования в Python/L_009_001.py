#! python
# coding=utf-8
# **************************************************************
# L_009_001.py
# 009.Логирование
# 001.Функции Логирования в Python
# --------------------------------------------------------------
# Практический Курс по Продвинутому Python (2023)
# https://www.udemy.com/course/avecoder-advanced-python/
# Ave Coder, 2023
# **************************************************************
# Writing by sgiman, May 2025

#---------------------------------------------------------------
# LOGGING:
# https://docs.python.org/3/library/logging.html
#---------------------------------------------------------------

# myapp.py (sample from docs)
import logging
import mylib

logger = logging.getLogger(__name__)

def main():
    logging.basicConfig(filename='myapp.log', level=logging.INFO)
    logger.info('Started')
    mylib.do_something()
    logger.info('Finished')

if __name__ == '__main__':
    main()
