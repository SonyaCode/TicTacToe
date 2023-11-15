import random
import colorama
from colorama import Fore
colorama.init(autoreset=True)

# functions

# prints out the board by 3x3
def print_board(board):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if col == len(board[0]) - 1:
                print(board[row][col])
            else:
                print(board[row][col], end=" |")
        if row < len(board) - 1:
            print("_________")


# check for available space by checking if the datatype in the space is a int
def check_for_available_space():
    available_space = [board[row][col] for row in range(3) for col in range(3) if isinstance(board[row][col], int)]
    return available_space

# player's and player 1's move
def player_move(position):
    while position not in check_for_available_space():
        print("This space is occupied")
        print()
        position = int(input("Enter your position: "))

    if position == 1 or position == 2 or position == 3:
        if isinstance(board[0][position - 1], int):
            board[0][position - 1] = Fore.GREEN + "X"
        else:
            print("This space is occupied.")
    elif position == 4 or position == 5 or position == 6:
        if isinstance(board[1][position - 4], int):
            board[1][position - 4] = Fore.GREEN + "X"
        else:
            print("This space is occupied.")
    elif position == 7 or position == 8 or position == 9:
        if isinstance(board[2][position - 7], int):
            board[2][position - 7] = Fore.GREEN + "X"
        else:
            print("This space is occupied")


# player 2's move
def player2_move(position):
    
    while position not in check_for_available_space():
        print("This space is occupied")
        print()
        position = int(input("Enter your position: "))

    if position == 1 or position == 2 or position == 3:
        if isinstance(board[0][position - 1], int):
            board[0][position - 1] = Fore.RED + "O"
        else:
            print("This space is occupied.")
    elif position == 4 or position == 5 or position == 6:
        if isinstance(board[1][position - 4], int):
            board[1][position - 4] = Fore.RED + "O"
        else:
            print("This space is occupied.")
    elif position == 7 or position == 8 or position == 9:
        if isinstance(board[2][position - 7], int):
            board[2][position - 7] = Fore.RED + "O"
        else:
            print("This space is occupied")


# computer's move
def computer_move():
    if len(check_for_available_space()) > 0:
        npc_position = random.choice(check_for_available_space())

        if npc_position == 1 or npc_position == 2 or npc_position == 3:
            board[0][npc_position - 1] = Fore.RED + "O"
        elif npc_position == 4 or npc_position == 5 or npc_position == 6:
            board[1][npc_position - 4] = Fore.RED + "O"
        elif npc_position == 7 or npc_position == 8 or npc_position == 9:
            board[2][npc_position - 7] = Fore.RED + "O"


# check win for player / player 1
def player_check_win(board):
    # all three horizontally occupied by "X", player wins
    if all(space == Fore.GREEN + "X" for space in board[0]) or all(space == Fore.GREEN + "X" for space in board[1]) or all(space == Fore.GREEN + "X" for space in board[2]):
        return True
    # all three vertically occupied by "X", player wins
    elif board[0][0] == board[1][0] == board[2][0] == Fore.GREEN + "X" or board[0][1] == board[1][1] == board[2][1] == Fore.GREEN + "X" or board[0][2] == board[1][2] == board[2][2]:
        return True
    # all three diagonally occupied by "X", player wins
    elif board[0][0] == board[1][1] == board[2][2] == Fore.GREEN + "X" or board[0][2] == board[1][1] == board[2][0] == Fore.GREEN + "X":
        return True


# check win for player 2 / computer
def player2_check_win(board):
    # all three horizontally occupied by "O", player 2 / computer wins
    if all(space == Fore.RED + "O" for space in board[0]) or all(space == Fore.RED + "O" for space in board[1]) or all(space == Fore.RED + "O" for space in board[2]):
        return True
    # all three vertically occupied by "O", player 2 / computer wins
    elif board[0][0] == board[1][0] == board[2][0] == Fore.RED + "O" or board[0][1] == board[1][1] == board[2][1] == Fore.RED + "O" or board[0][2] == board[1][2] == board[2][2]:
        return True
    # all three diagonally occupied by "O", player 2 / computer wins
    elif board[0][0] == board[1][1] == board[2][2] == Fore.RED + "O" or board[0][2] == board[1][1] == board[2][0] == Fore.RED + "O":
        return True



# MAIN PROGRAM
win = False
player1_win = False
player2_win = False
computer_win = False

# board
board = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]



print("Welcome to Tic-Tac-Toe!")
single_or_mult = int(input("[1] Single Player\n[2] Multiplayer\n"))

while single_or_mult != 1 and single_or_mult != 2:
    print("Error input.")
    single_or_mult = int(input("[1] Single Player\n[2] Multiplayer\n"))

print()
print_board(board)
print()
# single player
if single_or_mult == 1:

    # while win is false, keep playing
    while win == False:
        position = int(input("Enter your position: "))
        # ask player to move and print the board after the player chooses the move
        player_move(position)
        print()
        print_board(board)
        print()

        if player_check_win(board) == True:
            player1_win = True
            break # break the loop

        # tie
        if len(check_for_available_space()) == 0:
            break

        # computer moves and print the board
        print("Computer's turn!")
        computer_move()
        print()
        print_board(board)
        print()
        if player2_check_win(board) == True:
            computer_win = True
            break # break the loop



    if player1_win == True:
        print("You won!")
    elif computer_win == True:
        print("You lost! Computer won!")
    else:
        print("It's a tie!")


else:
    while win == False:
        # player 1's turn
        print("Player 1's turn!")
        player1_position = int(input("Enter your position: "))
        player_move(player1_position)
        print()
        print_board(board)
        print()
        
        # if player 1 wins, break the loop
        if player_check_win(board) == True:
            player1_win = True
            break

        # tie
        if len(check_for_available_space()) == 0:
            break

        # player 2's turn
        print("Player 2's turn!")
        player2_position = int(input("Enter your position: "))
        player2_move(player2_position)
        print()
        print_board(board)
        print()


        # if player 2 wins, break the loop
        if player2_check_win(board) == True:
            player2_win = True
            break



    if player1_win == True:
        print("Player 1 won!")
    elif player2_win == True:
        print("Player 2 won!")
    else:
        print("It's a tie!")