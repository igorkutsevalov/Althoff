try:
    a = input("введите число:")
    b = input("введите еще одно:")
    a = int(a)
    b = int(b)
    print(a / b)
except(ZeroDivisionError, ValueError):
    print("Ошибка ввода.")
