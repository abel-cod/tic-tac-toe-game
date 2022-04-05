# this will be tic tac toe game

current_player = "X"
board = ['-', '-', '-',
        '-','-','-',
        '-','-','-']
winner = ' '
# displaying the board
def show_board():
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('------------')
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('------------')
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])


# check if the input is already occupied
def check_place(input):
    if board[input] !='-':
        print("The place is already occupied")
        return False
    # we will place the user input in the position
    return True


# determine what will be the next player
def next_player():
    global current_player
    if current_player == "X":
        current_player = 'O'
    else: 
        current_player = "X"

# check if there is any row that has the same character and set to winner
def row():
    global winner
    if board[0] == board[1] == board[2] !='-':
        winner = board[0]
    elif board[3] == board[4] == board[5] != '-':
        winner = board[4]
    elif board[5] == board[7] == board[8] != '-':
        winner = board[7]
    else:
        # print("we have no the same value in row")
        return False    

    return winner

# check if there is any column that has the same character and set to winner
def column():
    global winner
    if board[0] == board[3] == board[6] != '-':
        winner = board[3]
    elif board[1] == board[4] == board[7] != '-':
        winner = board[4]
    elif board[2] == board[5] == board[8] != '-':
        winner = board[5]
    else:
        # print("we have no the same value in row")
        return False
    return winner

# check if there is any diagonal  that has the same character and set to winner
def diagonal():
    global winner
    if board[0] == board[4] == board[8] != '-':
        winner = board[4]
    elif board[2] == board[4] == board[6] != '-':
        winner = board[4]
    else:
    # print("we have no the same value in row")
        return False
    return winner


# if the board is full and there is no winner
def tie():
    #if row column and diagonal doesn't return winner there is no winner
    if not row() and column() and diagonal():
        return True
    # there is winner
    else:
        return False

# implementing the game logic
def game():
    global winner
    #run this until the board is full
    while not tie():
        # we will ask the user for input
        user_input = int(input("Enter the position: "))

        # we will check if the user input is not occupied
        if not check_place(user_input):
            user_input = int(input("Enter the position: "))

        board[user_input] = current_player
        show_board()
        
        # we will switch to the next player
        next_player()
        
        # store the return value of row column and diagonal 
        row_value = row()
        column_value = column()
        diagonal_value = diagonal()

        # if it return winner break out of loop for all row column and diagonal
        if row():
            print("The winner is " + row_value)
            break
        elif column():
            print("The winner is " + column_value)
            break
        elif diagonal():
            print("The winner is " + diagonal_value)
            break         



def main():
    game()


if __name__ == "__main__":
    main()

