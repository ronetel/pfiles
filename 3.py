num_one = int(input("Введите первое число"))
num_two = int(input("Введите второе число"))
print("Простые числа в данном диапазоне:")
for number in range(num_one, num_two + 1):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                break
        else:
            print(number)