# tic tac toe
# create board template, using format and args
# for args, declare an empty array, and append using format
# main while loop gives turns to X and Os
# checkWin checks for any winner.

print("Let's start X and O, with putting box numbers.. put number from 1 to 9, lie this.")

moves = ["1","2","3","4","5","6","7","8","9"]
board_template='''
_______
|{}|{}|{}|
|_____|
|{}|{}|{}|
|_____|
|{}|{}|{}|
'''
board = board_template.format(*moves)
print(board)
print("so lets starting putting your values, lets start with X first ")
moves = [" "," "," "," "," "," "," "," "," "]
board = board_template.format(*moves)
print(board)

def checkWin(player):
    board = board_template.format(*moves)
    print(board)
    # checkWin function, adds move in the board, and checks through 8 possibilites whether any winner,
    # if yes, then prints, and returns True, so the main While Loop breaks
    if(moves[0]==moves[1]==moves[2]==player):
        print(f"{player} is the winner")
        return True
    elif(moves[3]==moves[4]==moves[5]==player):
        print(f"{player} is the winner")
        return True
    elif (moves[6] == moves[7] == moves[8] == player):
        print(f"{player} is the winner")
        return True
    elif (moves[0] == moves[3] == moves[6] == player):
        print(f"{player} is the winner")
        return True
    elif (moves[1] == moves[4] == moves[7] == player):
        print(f"{player} is the winner")
        return True
    elif (moves[2] == moves[5] == moves[8] == player):
        print(f"{player} is the winner")
        return True
    elif (moves[0] == moves[4] == moves[8] == player):
        print(f"{player} is the winner")
        return True
    elif (moves[2] == moves[4] == moves[6] == player):
        print(f"{player} is the winner")
        return True
    else: return False


while True:
    X_input=int(input("which position do you want to put X "))
    moves[X_input]="X"
    if checkWin("X"): break
    O_input=int(input("which position do you want to put O "))
    moves[O_input]="O"
    if checkWin("Y"): break
