# Создайте программу для игры с конфетами человек против человека.
#
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
#  Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#
# a) Добавьте игру против бота
#
# b) Подумайте как наделить бота ""интеллектом""

import MyLibrary.CandyGameLib as my_lib
num_game = 0
isChanged = False
while not isChanged:
    num_game = input('Введите 1 для игры с напарником.\nВведите 2 для игры против бота.\nСделайте ваш выбор: ')
    if not num_game.isdigit():
        num_game = 0
    else:
        num_game = int(num_game)
    match int(num_game):
        case 1:
            print('Играем с другом')
            isChanged = True
        case 2:
            print('Играем с ботом')
            isChanged = True
        case _:
            print('Некорректный выбор игры.')

if num_game == 1: # Игра против человека
    first_player  = my_lib.Person('')
    second_player = my_lib.Person('')
    my_lib.game(first_player, second_player)

elif(num_game == 2): # Игра против бота
    first_player = my_lib.Person('')
    second_player = my_lib.Person('Bot')
    my_lib.game(first_player, second_player)

