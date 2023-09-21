from random import randint
print("Угадай число от 1 до 10")
x = randint(1,10)
popitka= 0

while True :
    num = int(input("Твой вариант:"))
    popitka += 1
    if num > x :
        print("Твое число больше")
    elif num < x :
        print("Твое число меньше")
    elif num == x :
        print(f"Молодец ты угадал число\n Колличество попыток : {popitka}\n Пока!")
        break