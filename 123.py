x = input ("Введите ваше имя: ")

Enter = ["Кароч ", "Это ", "Слушай "]
Reason = ["я простыла","я проспала","идет дождь", "не отгуляла отпуск", "Приболела", "Проспала", "Врос ноготь", "Потею как бегемот"]
Time = range(0,24)


import random

ent = random.choice(Enter)
reas = random.choice(Reason)
time = random.randint(0,24)

print("Привет {}.{},{}. Буду сегодня в {}".format(x, ent, reas, time))

