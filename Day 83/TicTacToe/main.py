import re

WELCOME_MESSAGE = '''
        #################################
        #                               #
        #    WELCOME TO TIC TAC TOE     #
        #                               #
        #                               #
        #                               #
        #         X  |  O  |  O         #
        #       -----+-----+-----       #
        #         O  |  X  |            #
        #       -----+-----+-----       #
        #         X  |  O  |  X         #
        #                               #
        #################################

Select your move by entering the row and column number. 
Ex: "1,3" for the top right position.

Let's get started!

========================================================
'''


def print_board(b: list[list]) -> None:
    """Prints the current state of the Tic-Tac-Toe board."""

    space = '      '
    for i, r in enumerate(b):
        print(space + '  ' + '  |  '.join(r) + '  ')
        if i < 2:
            print(space + '-----+-----+-----')


def is_valid_position(position_str: str) -> bool:
    """Returns True if the given string represents a valid board position, False otherwise."""

    pattern = r'^[1-3],[1-3]$'
    return bool(re.match(pattern, position_str))


def get_position(choice: str) -> tuple:
    """Converts a position string ('x,y') into a tuple of integers."""

    return int(choice.split(',')[0]) - 1, int(choice.split(',')[1]) - 1


def check_win(b: list[list], player: str) -> bool:
    """Returns True if the specified player has won the game, False otherwise."""

    for i in range(3):
        if b[i][0] == b[i][1] == b[i][2] == player:  # Check row
            return True
        if b[0][i] == b[1][i] == b[2][i] == player:  # Check column
            return True

    if b[0][0] == b[1][1] == b[2][2] == player:  # Top-left to bottom-right diagonal
        return True
    if b[0][2] == b[1][1] == b[2][0] == player:  # Top-right to bottom-left diagonal
        return True

    return False


def get_player_move(b, player: str) -> tuple:
    """Prompts the player for a board position and returns it as a tuple."""

    while True:
        position = input(f"Player '{player}', what is your move: ")
        if is_valid_position(position):
            r, c = get_position(position)
            if b[r][c] == ' ':
                return r, c
            else:
                print("This position has already been played!")
        else:
            print("Please enter a valid format.\nEx: '1,3' for the top right position.")


print(WELCOME_MESSAGE)
board = [[' ']*3 for _ in range(3)]

turn = 'X'
played = 0
while True:
    print_board(board)
    row, col = get_player_move(board, turn)
    board[row][col] = turn
    played += 1

    if check_win(board, turn):
        print_board(board)
        print(f"Player \"{turn}\" wins the game!")
        break

    if played == 9:
        print_board(board)
        print("We have a draw!")
        break

    # Switch player turn
    turn = 'O' if turn == 'X' else 'X'
