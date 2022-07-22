import random

pravila = '\nПравила игры:\nНа столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.\nПервый ход определяется жеребьёвкой.' \
          'За один ход можно забрать не более чем 28 конфет.\nВсе конфеты оппонента достаются сделавшему последний ход.\n'


class Person:

    def __init__(self, args: str):
        if args == 'Bot':
            self.name = args
            self.stupid = True if random.randint(0, 1) == 1 else False
            self.marker = ''
            if not self.stupid:
                print('Я умный бот, тебе хана. Ха ха ха!!')
            else:
                print('Я тупой бот, где я?')
        else:
            self.name = input('Введите ваше имя: ')

    def make_move(self, points: int) -> int:

        if self.name == 'Bot':
            if self.stupid:
                movve = random.randint(1, 28)
            else:
                movve = points % 29
        else:
            isChanged = False
            while not isChanged:
                movve = input(f'{self.name}, ведите число от 1 до 28: ')
                if not movve.isdigit():
                    print(f'{self.name}, вы ввели не число')
                    continue
                else:
                    movve = int(movve)
                    print(movve)
                    if movve < 1 or movve > 28:
                        print(f'{self.name} введенное число не в диапазоне 1 - 28. Введите его еще раз')
                    else:
                        isChanged = True
        return movve

    def set_marker(self, marker: str):
        self.marker = marker
        return move

    def tic_tac_move(self, tic_list: list, marker: str):
        isValid = False
        while not isValid:
            moove = input(f"{self.name} \"{self.marker}\", выберите номер поля.")

            if not moove.isdigit():
                print('Введенный символ не цифра!!!')
                continue

            moove = int(moove)
            if moove < 1 or moove > 9:
                print('Значение поля должно быть в диапазоне 1 - 9!!!')
                continue
            else:
                match moove:
                    case 1:
                        if self.reserved(tic_list[0][0]):
                            continue
                        tic_list[0][0] = marker
                    case 2:
                        if self.reserved(tic_list[0][1]):
                            continue
                        tic_list[0][1] = marker
                    case 3:
                        if self.reserved(tic_list[0][2]):
                            continue
                        tic_list[0][2] = marker
                    case 4:
                        if self.reserved(tic_list[1][0]):
                            continue
                        tic_list[1][0] = marker
                    case 5:
                        if self.reserved(tic_list[1][1]):
                            continue
                        tic_list[1][1] = marker
                    case 6:
                        if self.reserved(tic_list[1][2]):
                            continue
                        tic_list[1][2] = marker
                    case 7:
                        if self.reserved(tic_list[2][0]):
                            continue
                        tic_list[2][0] = marker
                    case 8:
                        if self.reserved(tic_list[2][1]):
                            continue
                        tic_list[2][1] = marker
                    case 9:
                        if self.reserved(tic_list[2][2]):
                            continue
                        tic_list[2][2] = marker

                isValid = True

    def reserved(self, value):
        if value == 'O' or value == 'X':
            print('Поле уже занято. Сделайте ваш выбор еще раз.')
            return True
        return False


def game(first_player: Person, second_player: Person):
    print(f'{first_player.name} и {second_player.name} в игре.\n{pravila}')
    who_plays = random.randint(1, 2)
    print(f'Игра начинается, и первым ходит {first_player.name if who_plays == 1 else second_player.name}')
    points = 2021
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
