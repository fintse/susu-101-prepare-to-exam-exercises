Num = int(input("Укажите номер места в плацкартном вагоне "))
if (Num > 54):
    print("Такого номера не существует, проверьте данные ")
    import sys
    sys.exit(0)
elif (Num > 0 and Num < 37):
    print("Ваше место в купе")
else:
    print("Ваше место - боковое")
if (Num % 2 == 0):
    print(", верхнее")
else:
    print(", нижнее")

