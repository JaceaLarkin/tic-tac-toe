def create_board():

    return [" ", " ", " ",
            " ", " ", " ",
            " ", " ", " "]

def show_board(board):
    print(board[0] + " | " + board[1] + " | " + board[2])

    print("---------")

    print(board[3] + " | " + board[4] + " | " + board[5])

    print("---------")

    print(board[6] + " | " + board[7] + " | " + board[8])

def player_move(board, player):
    while True:
        try:
            move = int(input(player + ", choose a space (1-9): "))

            if move < 1 or move > 9: 
                print("Not within 1-9 range")
                continue
            if board[move - 1] == " ":
                board[move - 1] = player
                break
            else:
                print("That space is taken")
        except ValueError:
            print("Enter a number")
            
def check_win(board, player):
    if board[0] == player and board[1] == player and board[2] == player:
        return True
    if board[6] == player and board[7] == player and board[8] == player:
        return True
    if board[3] == player and board[4] == player and board[5] == player:
        return True
    if board[0] == player and board[3] == player and board[6] == player:
        return True
    if board[1] == player and board[4] == player and board[7] == player:
        return True
    if board[2] == player and board[5] == player and board[8] == player:
        return True
    if board[0] == player and board[4] == player and board[8] == player:
        return True
    if board[2] == player and board[4] == player and board[6] == player:
        return True

    return False

def check_tie(board):
    if " " not in board:
        return True

    return False


def play_game():
    board = create_board()
    show_board(board)

    player = "X"

    while True:
        player_move(board, player)
        show_board(board)

        if check_win(board, player):
            print(player + " wins")
            break

        if check_tie(board):
            print("Its a tie")
            break

        if player == "X":
            player = "O"
        else: 
            player = "X"


play_game()
















































