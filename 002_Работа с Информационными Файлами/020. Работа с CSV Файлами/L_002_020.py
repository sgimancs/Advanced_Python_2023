#! python
# coding=utf-8
# ********************************************************
# L_002_020.py
# 002.Работа с Информационными Файлами
# 020.Работа с CSV Файлами
# --------------------------------------------------------
# Практический Курс по Продвинутому Python (2023)
# https://www.udemy.com/course/avecoder-advanced-python/
# Ave Coder, 2023
# ********************************************************
# Writing by sgiman, May 2025

import csv

print('-' * 128)
print(csv.list_dialects())  # диалекты CSV - ['excel', 'excel-tab', 'unix']
print('-' * 128)

#--------------------------------------------------------
# ЧТЕНИЕ CSV
#--------------------------------------------------------
def reader_sample():
    with open("customers-100.csv") as df:
        reader = csv.reader(df)
        for row in reader:
            print(row)

reader_sample()
print('-' * 128)

#--------------------------------------------------------
# РАБОР ДИАЛЕКТА CSV
#--------------------------------------------------------
def sniffer():
    with open("customers-100.csv") as snif:
        dialect = csv.Sniffer().sniff(snif.read(1024))
        snif.seek(0)
        has_header = csv.Sniffer().has_header(snif.read(1024))
        snif.seek(0)
        print("Headers: " + str(has_header))
        print(dialect.delimiter)                # разделители
        print(dialect.escapechar)               # ESC-символы
        print(dialect.quotechar)                # кавычки

sniffer()
print('-' * 128)

#--------------------------------------------------------
# ЗАПИСАТЬ CSV
#--------------------------------------------------------
# Index,Customer Id,First Name,Last Name,Company,City,Country,Phone 1,Phone 2,Email,Subscription Date,Website
def write_data():
    # Записать заголовок
    with open("customers-100-test.csv", mode="w") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Index,"
                             "Customer Id,"
                             "First Name,Last "
                             "Name,Company,"
                             "City,"
                             "Country,"
                             "Phone 1,"
                             "Phone 2,"
                             "Email,"
                             "Subscription Date,"
                             "Website"])

        # Записать строку данных
        csv_writer.writerow(["1","DD37Cf93aecA6Dc","Sheryl","Baxter","Rasmussen Group","East Leonard",
                             "Chile","229.077.5154","397.884.0519x718","zunigavanessa@smith.info",
                             "2020-08-24","http://www.stephenson.com/"])

write_data()
print('-end-' * 26)