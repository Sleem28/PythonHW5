import random

pravila = '\nПравила игры:\nНа столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.\nПервый ход определяется жеребьёвкой.' \
          'За один ход можно забрать не более чем 28 конфет.\nВсе конфеты оппонента достаются сделавшему последний ход.\n'


class Person:

    def __init__(self, args: str):
        if args == 'Bot':
            self.name = args
            self.stupid = True if random.randint(0, 1) == 1 else False
            if not self.stupid:
                print('Я умный бот, тебе хана. Ха ха ха!!')
            else:
                print('Я тупой бот, где я?')
        else:
            self.name = input('Введите ваше имя: ')

    def make_move(self, points: int) -> int:
        move = 0
        if self.name == 'Bot':
            if self.stupid:
                move = random.randint(1, 28)
            else:
                move = points % 29
        else:
            isChanged = False
            while not isChanged:
                move = input(f'{self.name}, ведите число от 1 до 28: ')
                if not move.isdigit():
                    print(f'{self.name}, вы ввели не число')
                    continue
                else:
                    move = int(move)
                    print(move)
                    if move < 1 or move > 28:
                        print(f'{self.name} введенное число не в диапазоне 1 - 28. Введите его еще раз')
                    else:
                        isChanged = True
        return move


def game(first_player: Person, second_player: Person):
    print(f'{first_player.name} и {second_player.name} в игре.\n{pravila}')
    who_plays = random.randint(1, 2)
    print(f'Игра начинается, и первым ходит {first_player.name if who_plays == 1 else second_player.name}')
    points = 50
    while points > 0:
        print(f'Текущее количество очков {points}')
        if who_plays == 1:
            points = move(first_player, points)
            who_plays = 2
        else:
            points = move(second_player, points)
            who_plays = 1

    if who_plays == 1:
        print(f'Выиграл игрок с именем {second_player.name}. ПОЗДРАВЛЯЕМ!!!')
    else:
        print(f'Выиграл игрок с именем {first_player.name}. ПОЗДРАВЛЯЕМ!!!')


def move(player: Person, points: int):
    print(f'Ходит {player.name}')
    moved = player.make_move(points)
    print(f'{player.name} походил {moved}.')
    points -= moved
    return points
