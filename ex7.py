# Дано натуральное число. Определить, будет ли это число: чётным, кратным 4.
num = input("Введите число для проверки ", )
num = int(num)

if num % 2 == 0 and num % 4 == 0:
    print("Число ",num, " четно и кратно 4")
else:
    print("Число не соответствует условию")