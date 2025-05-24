#! python
# coding=utf-8
# ***************************************************************
# L_002_026.py
# 002.Работа с Информационными Файлами
# 026.Работа с ZIP архивами
# ---------------------------------------------------------------
# Практический Курс по Продвинутому Python (2023)
# https://www.udemy.com/course/avecoder-advanced-python/
# Ave Coder, 2023
# ***************************************************************
# Writing by sgiman, May 2025

import zipfile
import os

# Создать и записать ZIP
z_name = "zip_archive.zip"
zip_file = zipfile.ZipFile(z_name, "w")
zip_file.write("./src/text_file_for_01.txt")
zip_file.write("./src/text_file_for_02.txt")
zip_file.write("./src/text_file_for_03.txt")

zip_file.close()
print(os.path.exists(z_name))

#####################################################################################
# Проверить наличие ZIP
# ZIP INSPECTOR - no worked !!!
# print(zip_file.is_zipfile("zip_archive.zip")) # ???
# zip_file = zipfile.ZipFile(z_name) # ???
# print(zip_file.namelist)
# print(zip_file.infolist)
# ..............................................
# РАСПАКОВАТЬ
#extract(zip_file)
#ip_file.extract(z_name) # ????
#z_name = "zip_archive.zip"
#zip_file = zipfile.ZipFile(z_name, "r")
#zip_file.extractall("./")
#####################################################################################

#-----------------------------------
#   Функция извлечения zip-файла
#-----------------------------------
def extract(zip_file2):
    file_name = zip_file2.split(".zip")[0]
    if zip_file2.endswith(".zip"):

        # Будет использовано для сохранения распакованного файла в текущем каталоге.
        current_working_directory = os.getcwd()                         # текущий директорий
        new_directory = current_working_directory + "/" + file_name     # новый директорий

        # Логика для распаковки файла
        with zipfile.ZipFile(zip_file2, 'r') as zip_object:
            zip_object.extractall(new_directory)
        print("Extracted successfully!!!")
    else:
        print("Not a zip file")


extract(z_name)     # распаковать
