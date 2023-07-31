import random
import time

def wait(time_waited):
    time.sleep(time_waited)

running = True
board = [
    '-','-','-',
    '-','-','-',
    '-','-','-'
]

board_rep = [
    0,0,0,
    0,0,0,
    0,0,0
]

#stuff

def display_board():
    print('__________________________________________')
    print(board[0] + '|' + board[1] + '|' + board[2])
    print(board[3] + '|' + board[4] + '|' + board[5])
    print(board[6] + '|' + board[7] + '|' + board[8])
    print('__________________________________________')

def players_choice():
    first = int(input('Enter a number: '))
    player_input = first - 1
    if board[player_input] != 'X' and board[player_input] != 'O':
        board[player_input] = 'X'
        board_rep[player_input] = 1

def computers_choice():
    computer_input = random.randint(0,8)
    if board[computer_input] != 'X' and board[computer_input] != 'O':
        board[computer_input] = 'O'
        board_rep[computer_input]= 20
    else:
        computers_choice()

def calculate_win():

    game_over = 0

    def board_full():
        full_or_not = False
        full_tiles = 0
        for item in board_rep:
            if item > 0:
                full_tiles += 1
        if full_tiles == 9:
            full_or_not = True
        return full_or_not

    board_is_full = board_full()

    if board_rep[0] + board_rep[1] + board_rep[2] == 3:
        print('Player wins!')
        game_over = 1
    elif board_rep[3] + board_rep[4] + board_rep[5] == 3:
        print('Player wins!')
        game_over = 1
    elif board_rep[6] + board_rep[7] + board_rep[8] == 3:
        print('Player wins!')
        game_over = 1
    elif board_rep[0] + board_rep[3] + board_rep[6] == 3:
        print('Player wins!')
        game_over = 1
    elif board_rep[1] + board_rep[4] + board_rep[7] == 3:
        print('Player wins!')
        game_over = 1
    elif board_rep[2] + board_rep[5] + board_rep[8] == 3:
        print('Player wins!')
        game_over = 1
    elif board_rep[0] + board_rep[4] + board_rep[8] == 3:
        print('Player wins!')
        game_over = 1
    elif board_rep[2] + board_rep[4] + board_rep[6] == 3:
        print('Player wins!')
        game_over = 1


    elif board_rep[0] + board_rep[1] + board_rep[2] == 60:
        print('Computer wins!')
        game_over = 1    
    elif board_rep[3] + board_rep[4] + board_rep[5] == 60:
        print('Computer wins!')
        game_over = 1
    elif board_rep[6] + board_rep[7] + board_rep[8] == 60:
        print('Computer wins!')
        game_over = 1
    elif board_rep[0] + board_rep[3] + board_rep[6] == 60:
        print('Computer wins!')
        game_over = 1
    elif board_rep[1] + board_rep[4] + board_rep[7] == 60:
        print('Computer wins!')
        game_over = 1
    elif board_rep[2] + board_rep[5] + board_rep[8] == 60:
        print('Computer wins!')
        game_over = 1
    elif board_rep[0] + board_rep[4] + board_rep[8] == 60:
        print('Computer wins!')
        game_over = 1
    elif board_rep[2] + board_rep[4] + board_rep[6] == 60:
        print('Computer wins!')
        game_over = 1
    
    else:
        if board_is_full:
            print('Draw!')
            game_over = 1

    return game_over

    



display_board()
print('You are playing Crosses')
wait(1)

while running:

    players_choice()

    wait(1)

    display_board()

    check = calculate_win()
    if check == 1:
        wait(1)
        break

    wait(1)

    calculate_win()

    check = calculate_win()
    if check == 1:
        wait(1)
        break

    wait(1)

    print("Computer's go...")

    wait(1)

    computers_choice()

    wait(1)

    display_board()

    check = calculate_win()
    if check == 1:
        wait(1)
        break

    wait(1)

    calculate_win()

    check = calculate_win()
    if check == 1:
        wait(1)
        break

    wait(1)
    

print('Thank you for playing!')
print('©2022 Noah Perrott')
