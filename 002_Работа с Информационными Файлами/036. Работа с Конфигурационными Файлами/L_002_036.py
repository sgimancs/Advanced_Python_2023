#! python
# coding=utf-8
# ********************************************************
# L_002_036.py
# 002.Работа с Информационными Файлами
# 036.Работа с Конфигурационными Файлами
# --------------------------------------------------------
# Практический Курс по Продвинутому Python (2023)
# https://www.udemy.com/course/avecoder-advanced-python/
# Ave Coder, 2023
# ********************************************************
# Writing by sgiman, May 2025

import configparser

config = configparser.ConfigParser()

config.read('config.cfg')

print('-' * 80)
print(config.sections())                                    # секции
print(config.has_section("Section 2"))                      # контроль секции
print('-' * 80)

UseTheLightSaber = bool(config['DEFAULT']['UseTheLightSaber'])    # value
print(UseTheLightSaber)
print(type(UseTheLightSaber))
print('-' * 80)

use_the_force = config['DEFAULT'].getboolean("UseTheLightSaber")
print(use_the_force)
#light_saber_power = config['DEFAULT'].getfloat('LightSaberPower')
light_saber_power = config['DEFAULT'].getint('LightSaberPower')
print(light_saber_power)
print('-' * 80)

# Обработка в случае ошибки
try:
    title = config['Section 3']['Title']
    print(title)
except KeyError as err:
    print("No such thing as")

print('-' * 80)
