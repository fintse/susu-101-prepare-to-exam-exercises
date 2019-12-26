# имя проекта: python exercises
# номер версии: 1.0
# имя файла: ex17.py
# автор и его учебная группа: Э.Финце, ЭУ-120
# дата создания: 29.11.2019
# дата последней модификации: 24.12.2019
# связанные файлы:
# описание: Имеются две ёмкости: кубическая с ребром A, цилиндрическая с высотой H и радиусом основания R.
# Определить, поместится ли жидкость объёма M в первую ёмкость, во вторую, в обе.
# версия Python: 3.7

import math
A = int(input("Ребро кубической ёмкости "))
R = int(input("Радиус основания цилиндрической ёмкости "))
H = int(input("Высота цилиндрической ёмкости "))
M = int(input("Объем жидкости "))

Sk = math.pow(A, 3)
print(Sk, "Объем куба")
Sc = ((math.pi) * (math.pow(R, 2)) * H)
print(Sc, "Объем цилиндра")
if (Sk + Sc > M ):
    print("Жидкость поместится в оба сосуда")
if (Sk >= M):
    print("Жидкость поместится в куб")
if (Sc >= M):
    print("Жидкость поместится в цилиндр")

