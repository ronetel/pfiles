import random as r
import time

dmg = r.randint(1, 6) / 2
hp = r.randint(1, 6) / 2
coins = r.randint(0,3)
srok_year = r.randint (0,3)
srok_mouth = r.randint (0,12)
def InitGame():
    age = r.randint(18,55)
    speshs = ["Любит постарше", "Злоупотребляет игрой в покер", "Работал во Вкусно и точка", "Коллекцианирует фантики от жвачек"]
    spesh = r.choice(speshs)
    osys = ["незаконный митинг", "вождение в нетрезвом состоянии", "убийство", "хранение наркотиков"]
    osy = r.choice(osys)
    name = input("Добро пожаловать в тюрягу, как твое имя салага?\n")
    print(f"Ну что, {name}, распологайся на зоне, вот твое дело:")
    print("-----------------------")
    print("Возраст: {0}".format(age))
    print("Особенность: {0}".format(spesh))
    print("Сила: {0} ".format(dmg))
    print("Здоровье: {0}".format(hp))
    print("Монеты: {0}. ".format(coins))
    print("Осужден за {0}".format(osy))
    print("Срок: {0}г.{1} мес.".format(srok_year,srok_mouth))

def Eat():
    global hp
    global srok_year
    global srok_mouth
    eats = ["гороховый суп", "парашу", "кашу"]
    eat = r.choice(eats)
    print(f"Вы попали в столовую, сегодня на ужин подают {eat}")
    nas = ["1.Возмутиться", "2.Молча схавать", "3.Насладиться пищей"]
    print("Ваши действия:")
    for item in nas:
        print(item)
    chose = int(input())
    if chose == 1:
        print("Вас угомонил охранник и вы отпраились в госпиталь, потеряв 1 здоровье")
        hp -= 1
        Hp()
    elif chose == 2:
        print("Вы давились едой и от этого вас вырвало - 0.5 здоровья")
        hp -= 0.5
        stat()
    elif chose == 3:
        hp += 0.5
        print(f"Вы с удовольствием похавали {eat}, ваше здоровье увеличилось на 0.5")
        stat()
    if srok_mouth == 0:
        srok_year -= 1
        srok_mouth = 12
    else:
        srok_mouth -= 1
    return srok_mouth


def con():
    global hp
    global srok_year
    global srok_mouth
    print("---------------------")
    sosed = ["1.-Вечер в хату", "2.Молча сесть на свободные нары", "3.-Мир вашему дому"]
    print("Ты оказался в камере, там сидит заключенный")
    print("Ваши действия:")
    for item in sosed:
        print(item)
    chose = int(input("Ваши действия: "))
    if chose == 1:
        print("-А не слишком ли ты борзый, молодой!?")
        print("Сосед оскорбился и избил вас, вы потеряли 0.5 здоровья")
        hp -= 0.5
        Hp()
    elif chose == 2:
        print("-Слышь фраерок, а ты хатой не ошибся?!")
        print("Знакомство с соседом не задалось")
        print("---------------------")
    elif chose == 3:
        print("-И вашему дому мир, проходи, садись, рассказывай как сам.")
        print("Вечер в компании сокамерника прошел чудесно")
        print("---------------------")
    else:
        print("Такого действия нет, попробуйте еще раз")
    if srok_mouth == 0:
        srok_year -= 1
        srok_mouth = 12
    else:
        srok_mouth -= 1
    return srok_mouth
    return srok_year

def Hp():
    global hp
    global  srok_year
    global srok_mouth
    print("---------------------")
    print("Вы попали в госпиталь")
    print(f"Ваше здоровье  {hp}")
    hospital = ["1.Спокойно отлежаться", "2.Искать приключения"]
    for item in hospital:
        print(item)
    chose = int(input())
    if chose == 1:
        print("Несколько блажнных дней пролетели незаметно и вы возвращаетесь в камеру")
        hp += 1
        print(f"Ваше здоровье улучшилось на 1 и равно {hp}")
        print("--------------------------")

    elif chose == 2:
        print("Какие к черту приключения, отлеживайся, у тебя сломаны ребра!!!")
        hp += 1
        print(f"Ваше здоровье улучшилось на 1 и равно {hp}")
        print("--------------------------")
    else:
        print("Такого действия нет, попробуйте еще раз")
    if srok_mouth == 0:
        srok_year -= 1
        srok_mouth = 12
    else:
        srok_mouth -= 1
    return srok_mouth
    return srok_year

def stat():
    print(f"У тебя {hp} жизней, {dmg} урона, {coins} монет")
    print("---------------------")
def Sport():
    global dmg
    global hp
    sport = ["1.Заниматься на тренажерах", "2.Играть в баскетбол", "3.Подойти к странному мужику"]
    print("---------------------")
    print("Вы попали в качалку")
    print("Ваши действия:")
    for item in sport:
        print(item)
    chose = int(input())
    if chose == 1:
        print("Вы подходите к штанге и начинаете тренировку")
        a = r.randint(0,3)
        if a == 0:
            print("Вы в поте лица занимались продолжительное время и улучшили силу на 0.5 ")
            dmg += 0.5
        elif a == 1:
            print("Вы слишком перенапряглись во время занятий")
            hp -= 5000
        else:
            print("Рядовая тренировка прошла без инцидентов")
            stat()
    elif chose == 2:
        print("Вы прекрасно провели время за игрой, ваше физическое состояние улучшилось + 0.5 к силе")
        dmg += 0.5
    elif chose == 3:
        kvest()
    return dmg
    return hp
def kvest():
    global name
    global coins
    if input(f"-Дарова чепух, хочешь подзаработать? да/нет").lower() == "да":
        print(f"Отлично, у меня для тебя есть особое задание, нужно будет собрать бычки от сигарет\n Принеси мне 100 бычков и получишь 5 золотых")
        print("---------------------")
        print("Вы отпарвились собирать бычки")
        i = 1
        while i != 100:
            i += 1
            print(f"Вы собрали {i} бычков")
            time.sleep(1)
        print("Хорош, мен ты собрал все нужные мне бычки, получай свои 5 монет")
        coins += 5
    else:
        print("-Жаль, приходи в другой раз")
def Meetshop():
    global hp
    global dmg
    global coins

    def buy(cost):
        if coins >= cost:
            coins -= cost
            print(f"У тебя {coins} монет")
            return True
        print("У тебя маловато золотых")
        return False
    itemss = {"Заточка": [10,20,30], "dkfkdm" : [20,30]}

def draka():
    global hp
    global coins
    global srok_year
    chelHP = r.randint(1,4)
    chelDMG = r.randint(1,3)
    chels = ["Лоха", "Нигера", "Качка", "Блатного"]
    chel = r.choice(chels)
    print("Добро пожаловать в клуб (бойцовский)")
    print(f"Сегодня на арене твой выбор пал на {chel}")
    print(f"У него {chelHP} хп и {chelDMG} едениц урона")
    print(f"У тебя {hp} жизней и {dmg} урона")
    print("Вы вступаете в бой")
    while chelHP >= 0 or hp >= 0:
        chose = input("Что будешь делать? (ударить/уклониться)").lower()
        if chose == "ударить":
            a = r.randint(1,3)
            if a == 1:
                chelHP -= dmg
                print(f"Ты успешно атаковал {chel} и у него осталось {chelHP} хп")
            elif a == 2:
                print("К сожалению противник увернулся от удара")
            else:
                hp -= chelDMG
                print(f"Эх, ты пропустил удар, у тебя осталось {hp} хп")

        elif chose == "уклониться":
            b = r.randint(1,3)
            if b == 1:
                chelHP -= dmg
                print(f"Ты успешно увернулся от удара {chel}, да и к тому же конт атаковал его, у него осталось {chelHP} хп")
            elif b == 2:
                print("Ты успешно увернулся от удара")
            else:
                hp -= chelDMG
                print(f"Эх, тебе не удалось увернуться, у тебя осталось {hp} хп")
        else:
            continue
        if chelHP <= 0:
            loot = r.randint(0,2) + chelHP
            coins += loot
            print(f"Супер ты победил {chel}, за это ты получаешь {loot} монет, но так же из-за драки ваш срок увеличили на 1 г.")
            srok_year += 1
            stat()
            break
        elif hp <= 0:
            break
    return hp
    return srok_year

InitGame()
con()
while True:
    if hp <= 0:
        print("Вы умерли(((")
        if input("Хотите начать заного? да/нет ").lower() == "да":
            hp = r.randint(1, 6) / 2
            InitGame()
        else:
            print("Ну и пожалуйста")
            break
    situation = r.randint(0, 10)
    print(f"Осталось отматать {srok_year}г. {srok_mouth} мес.")
    if situation == 0:
        Eat()
    elif situation == 1:
        draka()
    elif situation == 2:
        Sport()
    else:
        if srok_mouth == 0:
            srok_year -= 1
            srok_mouth = 12
        else:
            srok_mouth -= 1

        input(f"Мотаю срок...")
    if srok_year == 0 and srok_mouth == 0:
        print("ПОЗДРАВЛЯЮ!!!")
        print("Вы отсидели срок, можете быть свободны")
        if input("Ну или все таки хотите начать заного? да/нет ").lower() == "да":
            hp = r.randint(1, 6) / 2
            dmg = r.randint(1, 6) / 2
            hp = r.randint(1, 6) / 2
            coins = r.randint(1,3)
            srok_year = r.randint (0,3)
            srok_mouth = r.randint (0,12)
            InitGame()
            con()
        else:
            print("Досвидос)))")
            break