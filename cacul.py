import math
print(" 1. Сложение\n 2. Вычитание \n 3. Умножение \n 4. Деление \n 5. Возведение в степень \n 6. Квадратный корень \n 7. Факториал \n 8. Синус \n 9. Косинус \n 10. Тангенс")

while True:
    try:
        num = int(input("Выберите действие: "))
        if num in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
            if num == 1:
                x = float(input("Введите первое число "))
                y = float(input("Введите второе число "))
                print("Ваше число: ", x + y)

            if num == 2:
                x = float(input("Введите первое число "))
                y = float(input("Введите второе число "))
                print("Ваше число: ", x - y)


            if num == 3:
                x = float(input("Введите первое число "))
                y = float(input("Введите второе число "))
                print("Ваше число: ", x * y)

            if num == 4:
                x = float(input("Введите первое число "))
                y = float(input("Введите второе число "))
                if y == 0:
                    print("чечик, на ноль делить нельзя")
                else:
                    print("Ваше число", x / y)

            if num == 5:
                x = float(input("Введите число "))
                y = float(input("Введите степень "))
                print("Ваше число: ", x ** y)

            if num == 6:
                x = float(input("Введите число "))
                sqrt = math.sqrt(x)
                print("Квадратный корень из числа " + str(x) + " это " + str(sqrt))

            if num == 7:
                x = int(input("Введите число "))
                print("Факориал числа", x, "это", + math.factorial(x))

            if num == 8:
                x = int(input("Введите число "))
                print("Синус числа", x, "это", + math.sin(x))

            if num == 9:
                x = int(input("Введите число "))
                print("Косинус числа", x, "это", + math.cos(x))

            if num == 10:
                x = int(input("Введите число "))
                print("Тангенс числа", x, "это", + math.tan(x))
        else:
            print(" чечик операции нет")
    except ValueError:
        print(" чечик, пиши цифрами")
