from random import randint

board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print "Let's play Battleship!"
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship1_row = random_row(board)
ship1_col = random_col(board)

ship2_row = random_row(board)
ship2_col = random_row(board)
print "Ship1_row %d" %(ship1_row)
print "ship1_col %d" %(ship1_col)
print "ship2_row %d" %(ship2_row)
print "ship2_col %d" %(ship2_col)

# Everything from here on should go in your for loop!
# Be sure to indent four spaces!
for turn in range(4):
    print 
    print
    print "You are on your %d chance" %(turn)


    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))

    
    if (guess_row == ship1_row and guess_col == ship1_col):
        if (guess_row == ship2_row and guess_col == ship2_col):

            print "Congratulations! You sunk all the battleships!"
            board[guess_row][guess_col] = "W!"
            break
        # print_board(board)
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
            if turn == 3:
                print "Game Over"
            # print_board(board)
        elif(board[guess_row][guess_col] == "X"):
          print
          print "You guessed that one already."
          if turn == 3:
            print "Game Over"
          # print_board(board)
        else:
            print
            print "You missed my battleship!"
            print turn
            board[guess_row][guess_col] = "X"
            if turn == 3:
                print "Game Over"

    
    # Print (turn + 1) here!
    # print "you have completed %d chance" %(turn+1)
print_board(board)