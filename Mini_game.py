"""Написать игру. Пользователь должен угадать число.
Сперва вводиться диапазон угадывания. После
колличество попыток. В случае правильного ответа -
выводить You are the winner. В случае неправильного
давать игроку подсказку(больше или меньше искомое
число). Если за указанное количество попыток число не
угадано - выводить: You are the loser и правильное число."""

import  random
number_a = int(input('a = '))
number_b = int(input('b = '))
kol_popitok = int(input('kol_popitor = '))
number = random.randint(number_a, number_b)
while True:
    if kol_popitok < 1:
        print(f'You are the loser! Number = {number}')
        break
    number_x = int(input('Enter number = '))

    if number_x == number:
        print(f'You are the winner! = {number}')
        break
    elif number_x < number:
        print(f'Искомое число больше {number_x}')
    else:
        print(f'Искомое число меньше {number_x}')
    kol_popitok -= 1
