# Создайте программу для игры в ""Крестики-нолики"".
import random

import MyLibrary.CandyGameLib as my_lib


def draw_board(board: list):
    print("-------------")
    line = 3
    for i in range(line):
        print("|", board[i][0], "|", board[i][1], "|", board[i][2], "|")
        print("-------------")


def win(board: list[[]], symbol: str) -> bool:
    if board[0][0] == board[0][1] == board[0][2] == symbol or \
            board[1][0] == board[1][1] == board[1][2] == symbol or \
            board[2][0] == board[2][1] == board[2][2] == symbol or \
            board[0][0] == board[1][0] == board[2][0] == symbol or \
            board[0][1] == board[1][1] == board[2][1] == symbol or \
            board[0][2] == board[1][2] == board[2][2] == symbol or \
            board[0][0] == board[1][1] == board[2][2] == symbol or \
            board[0][2] == board[1][1] == board[2][0] == symbol:
        return True
    else:
        return False


def draw_between(tic_list: list) -> bool:
    for item in tic_list:
        if str(item[0]).isdigit() or str(item[1]).isdigit() or str(item[2]).isdigit():
            return False
    return True


tic_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

end = False
first_win = False
second_win = False
draw_win = False
next_p = 0

print(f'Игра крестики-нолики.\n')
print('Игрок 1.', end=' ')
first_player = my_lib.Person('')
print('Игрок 2.', end=' ')
second_player = my_lib.Person('')
print(f'Игрок {first_player.name} играет "O"')
first_player.set_marker('O')
print(f'Игрок {second_player.name} играет "X"\n')
second_player.set_marker('X')
print('Выберем, кто будет ходить первым рандомно.')
next_p = random.randint(1, 2)
print(f'Первым ходит игрок с именем {first_player.name if next_p == 1 else second_player.name}\n')
print(
    'Правила игры: Текущий игрок выбирает поле из таблицы и помечает его своим маркером.\nЗа ним ходит следующий игрок '
    'и помечает сободное поле своим маркером.\nСвободные поля пронумерованы цифрами.\nКто быстрее промаркирует все поля '
    'в линию по горизонтали вертикали или по диагонали, тот и выиграл.')

while not end:
    draw_board(tic_list)
    if next_p == 1:
        first_player.tic_tac_move(tic_list, first_player.marker)
        if win(board=tic_list, symbol=first_player.marker):
            end = True
            first_win = True
        next_p = 2
    else:
        second_player.tic_tac_move(tic_list, second_player.marker)
        if win(board=tic_list, symbol=second_player.marker):
            end = True
            second_win = True
        next_p = 1
    if draw_between(tic_list):
        draw_win = True
        end = True

draw_board(tic_list)
if first_win:
    print(f'Игрок с именем {first_player.name} победил!!!')
elif second_win:
    print(f'Игрок с именем {second_player.name} победил!!!')
elif draw_win:
    print('Ничья!!!')
