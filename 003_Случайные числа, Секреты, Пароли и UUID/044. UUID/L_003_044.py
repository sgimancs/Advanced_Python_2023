#! python
# coding=utf-8
# ********************************************************
# L_003_044.py
# 003_Случайные числа, Секреты, Пароли и UUID
# 044.UUID
# --------------------------------------------------------
# Практический Курс по Продвинутому Python (2023)
# https://www.udemy.com/course/avecoder-advanced-python/
# Ave Coder, 2023
# ********************************************************
# Writing by sgiman, May 2025

# UUID - используется для идентификации информации,которая должна быть уникальной
# RFC 4122

import uuid

result_uuid4 = uuid.uuid4()

# UUID4 (популярный формат)
print('-' * 80)
print("UUID4: ")
print(result_uuid4)
print(result_uuid4.hex)
print(result_uuid4.urn)
print('-' * 80)

# UUID5 (рекомендуемый формат)
result_uuid5 = uuid.uuid5(uuid.NAMESPACE_DNS, "sgiman.com")
print("UUID5: ")
print(result_uuid5)
print(result_uuid5.hex)
print(result_uuid5.urn)
print('-' * 80)
