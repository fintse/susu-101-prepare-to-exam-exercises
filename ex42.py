# имя проекта: python exercises
# номер версии: 1.0
# имя файла: ex42.py
# автор и его учебная группа: Э.Финце, ЭУ-120
# дата создания: 29.11.2019
# дата последней модификации: 24.12.2019
# связанные файлы:
# описание: Дан одномерный массив числовых значений, насчитывающий N элементов.
# Определить, образуют ли элементы массива, расположенные перед первым
# отрицательным элементом, возрастающую последовательность.
# версия Python: 3.7



import random

N = int(input("Количество элементов массива"))
A = [1,5,3,-4]
print(A)
a = 0

for i in range(N):
    if A[i] >= 0:
        break
    if A[i] < 0:
        for i in range(N):
            if A[i-1] < A[i]:
                a = 0
            else:
                a =1
                break
        A[i] = A[i] - 1

if (a == 0):
    print("Возрастающая")
else:
    print("Убывающая")