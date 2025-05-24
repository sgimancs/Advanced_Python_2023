#! python
# coding=utf-8
# ********************************************************
# L_001_017.py
# 001.Разогрев
# 017.Функция all()
# --------------------------------------------------------
# Практический Курс по Продвинутому Python (2023)
# https://www.udemy.com/course/avecoder-advanced-python/
# Ave Coder, 2023
# ********************************************************
# Writing by sgiman, May 2025

print('-' * 80)

# Variant 1
def valid_rgb_1(rgb):
    # Check if rgb input tuple is within 0-255
    for val in rgb:
        if not 0 <= val <= 255:
            return False
    return True


print(valid_rgb_1((255, 100, 255)))
print(valid_rgb_1((255, 100, 256)))
print('-' * 80)

# Variant 2
def valid_rgb_2(rgb):
    # Check if rgb input tuple is within 0-255
    # Список
    valid = [
        0 <= val <= 255
        for val in rgb
    ]
    return all(valid)   # all()

print(valid_rgb_2((255, 100, 255)))
print(valid_rgb_2((255, 100, 256)))
print('-' * 80)


###### ALL ######
# Variant 3
def valid_rgb_3(rgb):
    # Check if rgb input tuple is within 0-255
    # all()
    return all(
        0 <= val <= 255
        for val in rgb
    )

print(valid_rgb_3((255, 100, 255)))
print(valid_rgb_3((255, 100, 256)))
print('-' * 80)

