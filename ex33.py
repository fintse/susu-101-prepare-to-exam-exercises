# имя проекта: python exercises
# номер версии: 1.0
# имя файла: ex33.py
# автор и его учебная группа: Э.Финце, ЭУ-120
# дата создания: 29.11.2019
# дата последней модификации: 24.12.2019
# связанные файлы:
# описание: Дан одномерный массив числовых значений, насчитывающий N элементов.
# Выполнить перемещение элементов массива по кругу вправо, т. е. A[1] → A[2]; A[2] → A[3]; ... A[n] → A[1].
# версия Python: 3.7



import random

N = int(input("Введите количество элементов массива "))
a = [random.randint(0, 100) for i in range(0,N)]
print(a)

if (len(a) % 2 == 1):
    end = N
else:
    end = N-1


for i in range(end-1):
    a[i], a[i + 1] = a[i + 1], a[i]
print(a)
