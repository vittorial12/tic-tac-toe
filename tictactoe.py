import os
import random

def get_player_chars():
    player1 = input('Please enter player1 character: ')
    player2 = input('Please enter player2 character: ')
    print()

    while player1 == player2:
        print('Error. Users cannot have same character.')
        player1 = input('Please enter player1 character: ')
        player2 = input('Please enter player2 character: ')
        print()

    return player1, player2

def create_board():
    board = []

    for i in range(3):
        row = []
        board.append(row)
        for j in range(3):
            row.append(' ') 
            
    return board

def print_board(board):
    os.system('clear')

    print('Tic Tac Toe Game\n')

    for i in range(3):
        print('-------------')
        for j in range(3):
            print('|', board[i][j], end=' ')
        print('|')
    print('-------------')   

def switch_players(current_player):
    if current_player == 1:
        return 2
    else:
        return 1

def get_coordinates(board):
    x = int(input('Please enter the x coordinate: '))
    y = int(input('Please enter the y coordinate: '))
    print()

    while not are_coordinates_valid(board, (x, y)):
        print('The coordinates ({}, {}) are not valid!'.format(x, y))
        x = int(input('Please enter the x coordinate: '))
        y = int(input('Please enter the y coordinate: '))
        print()

    return x, y

def is_position_empty(board, coordinates):
    x, y = coordinates
    return board[x][y] == ' '

def are_coordinates_valid(board, coordinates):
    x, y = coordinates
    return (x >= 0 and x < 3) and (y >= 0 and y < 3) and is_position_empty(board, coordinates)

def update_board(board, coordinates, players_char):
    x, y = coordinates
    board[x][y] = players_char


def check_row_win(board, players_char):

    for row in board:
        if row == [players_char] * 3:
            return True    
    return False

def check_col_win(board, players_char):
    for i in range(3):
        col = [board[0][i], board[1][i], board[2][i]]
        if col == [players_char] * 3:
            return True
    return False

def check_diagonal_win(board, players_char):
    diagonal1 = [board[0][0], board[1][1], board[2][2]]
    diagonal2 = [board[0][2], board[1][1], board[2][0]]

    if diagonal1 == [players_char] * 3 or diagonal2 == [players_char] * 3:
        return True
    else:
        return False

def is_game_over(board, move_count, current_player, players_char):
    game_over = False

    if move_count == 9:
        print_board(board)
        print('\nTie!')
        print('The Game is Over!\n')
        game_over = True
    else:
        if (check_row_win(board, players_char) or 
            check_col_win(board, players_char) or
            check_diagonal_win(board, players_char)):

            print_board(board)
            print('\nPlayer{} has won!'.format(current_player))
            print('The Game is Over!\n')
            game_over = True

    return game_over

def main():
    players = get_player_chars()
    current_player = random.randint(1, 2)
    move_count = 0
    board = create_board()

    while True:
        print_board(board)
        print("\nIt is player{}'s turn".format(current_player))
        coordinates = get_coordinates(board)
        update_board(board, coordinates, players[current_player - 1])
        move_count += 1

        if is_game_over(board, move_count, current_player, players[current_player - 1]):
            break

        current_player = switch_players(current_player)
         
     
main()


