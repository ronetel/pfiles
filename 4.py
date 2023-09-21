num = int(input ("Введите число таблицу которого вы хотите узнать: "))
c = 1
print ("Таблица умножения числа: ", num)
while c <= 10:
    num = num * 1
    print (num, 'x', c, '=', num * c)
    c += 1