#! python
# coding=utf-8
#############################################################
# log_calculate.py
# Основы Python — кратко. Часть 4. Генераторы списков (2008)
# https://habr.com/ru/articles/30232/
#############################################################
# Writing by sgiman, May 2025

# import ...

# 1 считываем из файла строки и делим их на пары IP-адрес
raw = [x.split(" ") for x in open("log.txt")]   # открыть-прочитать(open) и разделить(split)

# 2 заполняем словарь
rmp = {}
for ip, traffic in raw:
        if ip in rmp:
                rmp[ip] += int(traffic)
        else:
                rmp[ip] = int(traffic)

# 3 переводим в список и сортируем
lst = rmp.items()
#lst.sort(key = lambda key, val: key)   # python 2 (?)

# 4 получаем результат
print('=' * 80)
print ("\n".join(["%s\t%d" % (host, traff) for host, traff in lst]))    # python 2

print('=' * 80)
print ('\n'.join([f"{host}\t{traff}" for host, traff in lst]))          # python 3
