# имя проекта: python exercises
# номер версии: 1.0
# имя файла: ex52.py
# автор и его учебная группа: Э.Финце, ЭУ-120
# дата создания: 29.11.2019
# дата последней модификации: 24.12.2019
# связанные файлы:
# описание: Заданы M строк символов, которые вводятся с клавиатуры.
# Из заданных строк, каждая из которых представляет одно слово, составить одну длинную строку, разделяя слова пробелами.
# версия Python: 3.7

M = 4

list_strings = []

for i in range(0, M):
    print("Введите строку:", end=' ')
    list_strings.append(input())

print(' '.join(list_strings))