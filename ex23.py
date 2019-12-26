# имя проекта: python exercises
# номер версии: 1.0
# имя файла: ex23.py
# автор и его учебная группа: Э.Финце, ЭУ-120
# дата создания: 29.11.2019
# дата последней модификации: 24.12.2019
# связанные файлы:
# описание: Даны двещественные числа X и Y . Вычислить Z. Z = √(X x Y) при X > Y, Z = ln(X + Y ) в противном случае.
# версия Python: 3.7

import math
X = float(input("Введите вещественное число X "))
Y = float(input("Введите вещественное число Y "))

if X > Y:
    Z = math.sqrt(X * Y)
    print(Z," =")
else:
    Z = math.log(X + Y, math.e)
    print(Z," =")