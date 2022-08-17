data = {'Путин': '1952', 'Шойгу': '1955', 'Байден': '1942', 'Обама': '1961', 'Ельцин': '1931'}

correct_answers = 0

wrong_answers = 0

count = 0

flag = True

while flag:

    for item in data.items():

        bornyear = input(f'В каком году родился {item[0]}?  ')

        if bornyear == item[1]:
            correct_answers += 1
        else:
            wrong_answers += 1

        count += 1

    print(f'кол-во ошибок: {wrong_answers}',
          f'кол-во правильных ответов: {correct_answers}',
          f'Процент правильных ответов {(correct_answers/count)*100}%',
          f'Процент неправильных ответов {(wrong_answers/count)*100}%',
          sep='\n')

    replay = input('Хотите повторить?(Да\Нет) ')

    if replay == 'Да':

        correct_answers = 0

        wrong_answers = 0

        count = 0

        flag = True
    else:
        flag = False

        print('Спасибо за игру! Пока!')







