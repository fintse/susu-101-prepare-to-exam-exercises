# имя проекта: python exercises
# номер версии: 1.0
# имя файла: ex62.py
# автор и его учебная группа: Э.Финце, ЭУ-120
# дата создания: 29.11.2019
# дата последней модификации: 24.12.2019
# связанные файлы:
# описание: Определить сумму вводимых положительных чисел. Причём числа с нечётными номерами
# (по порядку ввода) суммировать с обратным знаком, а числа с чётными номерами перед суммированием возводить в квадрат.
# Подсчитать количество слагаемых. При вводе первого отрицательного числа закончить работу.
# версия Python: 3.7

import re

list_numbers = []

sum = 0
sum_count = 0


i = 1
while True:
    print("Введите число:", end=' ')
    string = re.sub(r'[^0-9\-]+', '', input())
    if len(string) == 0:
        print("В строке не обнаружено числа")
        continue

    number = int(string)
    list_numbers.append(number)

    if i % 2 != 0:
        number *= -1
    else:
        number *= number

    sum += number
    i += 1
    if list_numbers[len(list_numbers) - 1] < 0:
        break


print("Сумма:", sum)
print("Количество слагаемых:", i)
