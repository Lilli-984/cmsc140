# I can't remember my groupmates' names! I was sitting at table 4 I think.
#I typed the second half of the code!


board = {"A": [".", ".", "."], "B": [".", ".", "."], "C": [".", ".", "."]}


def print_board(board):
    print("\n Current Board: \n")
    print("     A    B    C")
    for i in range(len(board.values())):
        print(str(i+1) + "    " + board["A"][i] + "    " +  board["B"][i] + "    " + board["C"][i])
    print("\n")

def battleship(board): 
    print("Welcome to Battleship!")

    print("Player 1, select a column for your battleship: ")
    column = input()
    print("Player 1, select a row for your battleship: ")
    row = int(input())
    print_board(board)
    guesses = 0
    print("Player 2, select a column to check: ")
    column_2 = input()
    print("Player 2, select a row to check: ")
    row_2 = int(input())
    guesses += 1
    print_board(board)
    while column_2 != column or row_2 != row:
        board[column_2][row_2-1]= "x"
        print("Sorry, theres nothing there. \n")
        print_board(board)
        guesses += 1
        
        print("Player 2, select a column to check: ")
        column_2 = input()
        print("Player 2, select a row to check: ")
        row_2 = int(input())
        print_board(board)

    board[column_2][row_2-1] = "!"
    guesses += 1
    print("You won!")

    print_board(board)
    print("Score: ",guesses, "Guesses")
        
battleship(board)