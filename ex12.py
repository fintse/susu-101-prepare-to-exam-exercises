# имя проекта: python exercises
# номер версии: 1.0
# имя файла: ex12.py
# автор и его учебная группа: Э.Финце, ЭУ-120
# дата создания: 29.11.2019
# дата последней модификации: 24.12.2019
# связанные файлы:
# описание: Дано вещественное число. Определить, какое это число: положительное, отрицательное, ноль.
# версия Python: 3.7

num1 = float(input("Введите вещественное число "))

if (num1 == 0):
    print("Число равно 0 ")
elif (num1 > 0):
    print("Число положительное ")
elif (num1 < 0):
    print("Число отрицательное ")

