bornyear = input('В каком году родился Пушкин?  ')
if bornyear == '1799':
    bornday = input('В какой день родился Пушкин?  ')
    if bornday == '6 июня':
        print('Верно')
    else:
        print('Неверный день рождения')
else:
    print('Неверно')