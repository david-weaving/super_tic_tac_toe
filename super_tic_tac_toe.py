

# rough version of tic tac toe to played in the console

tc_top_left = [1,2,3,4,5,6,7,8,9]
tc_top_middle = [1,2,3,4,5,6,7,8,9]
tc_top_right = [1,2,3,4,5,6,7,8,9]
tc_left_middle = [1,2,3,4,5,6,7,8,9]
tc_middle_middle = [1,2,3,4,5,6,7,8,9]
tc_right_middle = [1,2,3,4,5,6,7,8,9]
tc_bottom_left = [1,2,3,4,5,6,7,8,9]
tc_bottom_middle = [1,2,3,4,5,6,7,8,9]
tc_bottom_right = [1,2,3,4,5,6,7,8,9]


the_game = [tc_top_left,tc_top_middle,tc_top_right,tc_left_middle,tc_middle_middle,tc_right_middle,tc_bottom_left,tc_bottom_middle,tc_bottom_right]


def turn(n):
    x_o = n % 2
    if x_o == 0:
        return 'X'
    else:
        return 'O'
    
def update_board(next_spot):
    print(f"|{the_game[next_spot][0]}|{the_game[next_spot][1]}|{the_game[next_spot][2]}|")
    print(f"|{the_game[next_spot][3]}|{the_game[next_spot][4]}|{the_game[next_spot][5]}|")
    print(f"|{the_game[next_spot][6]}|{the_game[next_spot][7]}|{the_game[next_spot][8]}|")

def show_entire_board():
    print(f"||{the_game[0][0]}||{the_game[0][1]}||{the_game[0][2]}||   ||{the_game[1][0]}||{the_game[1][1]}||{the_game[1][2]}||   ||{the_game[2][0]}||{the_game[2][1]}||{the_game[2][2]}||")
    print(f"||{the_game[0][3]}||{the_game[0][4]}||{the_game[0][5]}||   ||{the_game[1][3]}||{the_game[1][4]}||{the_game[1][5]}||   ||{the_game[2][3]}||{the_game[2][4]}||{the_game[2][5]}||")
    print(f"||{the_game[0][6]}||{the_game[0][7]}||{the_game[0][8]}||   ||{the_game[1][6]}||{the_game[1][7]}||{the_game[1][8]}||   ||{the_game[2][6]}||{the_game[2][7]}||{the_game[2][8]}||\n")

    print(f"||{the_game[3][0]}||{the_game[3][1]}||{the_game[3][2]}||   ||{the_game[4][0]}||{the_game[4][1]}||{the_game[4][2]}||   ||{the_game[5][0]}||{the_game[5][1]}||{the_game[5][2]}||")
    print(f"||{the_game[3][3]}||{the_game[3][4]}||{the_game[3][5]}||   ||{the_game[4][3]}||{the_game[4][4]}||{the_game[4][5]}||   ||{the_game[5][3]}||{the_game[5][4]}||{the_game[5][5]}||")
    print(f"||{the_game[3][6]}||{the_game[3][7]}||{the_game[3][8]}||   ||{the_game[4][6]}||{the_game[4][7]}||{the_game[4][8]}||   ||{the_game[5][6]}||{the_game[5][7]}||{the_game[5][8]}||\n")

    print(f"||{the_game[6][0]}||{the_game[6][1]}||{the_game[6][2]}||   ||{the_game[7][0]}||{the_game[7][1]}||{the_game[7][2]}||   ||{the_game[8][0]}||{the_game[8][1]}||{the_game[8][2]}||")
    print(f"||{the_game[6][3]}||{the_game[6][4]}||{the_game[6][5]}||   ||{the_game[7][3]}||{the_game[7][4]}||{the_game[7][5]}||   ||{the_game[8][3]}||{the_game[8][4]}||{the_game[8][5]}||")
    print(f"||{the_game[6][6]}||{the_game[6][7]}||{the_game[6][8]}||   ||{the_game[7][6]}||{the_game[7][7]}||{the_game[7][8]}||   ||{the_game[8][6]}||{the_game[8][7]}||{the_game[8][8]}||\n")

def check_entire_tile(board_tracker,x_o): # checks to see if a tile has been won by and X or O and completely fills it in
    if the_game[board_tracker][0] == the_game[board_tracker][1] == the_game[board_tracker][2]:
        print(f"Tile {board_tracker + 1} has been taken!")
        for i in range(len(the_game)):
            the_game[board_tracker][i] = x_o
    
    elif the_game[board_tracker][3] == the_game[board_tracker][4] == the_game[board_tracker][5]:
        print(f"Tile {board_tracker + 1} has been taken!")
        for i in range(len(the_game)):
            the_game[board_tracker][i] = x_o
    
    elif the_game[board_tracker][6] == the_game[board_tracker][7] == the_game[board_tracker][8]:
        print(f"Tile {board_tracker + 1} has been taken!")
        for i in range(len(the_game)):
            the_game[board_tracker][i] = x_o
    
    elif the_game[board_tracker][0] == the_game[board_tracker][4] == the_game[board_tracker][8]:
        print(f"Tile {board_tracker + 1} has been taken!")
        for i in range(len(the_game)):
            the_game[board_tracker][i] = x_o
    
    elif the_game[board_tracker][2] == the_game[board_tracker][4] == the_game[board_tracker][6]:
        print(f"Tile {board_tracker + 1} has been taken!")
        for i in range(len(the_game)):
            the_game[board_tracker][i] = x_o

    elif the_game[board_tracker][0] == the_game[board_tracker][3] == the_game[board_tracker][6]:
        print(f"Tile {board_tracker + 1} has been taken!")
        for i in range(len(the_game)):
            the_game[board_tracker][i] = x_o

    elif the_game[board_tracker][1] == the_game[board_tracker][4] == the_game[board_tracker][7]:
        print(f"Tile {board_tracker + 1} has been taken!")
        for i in range(len(the_game)):
            the_game[board_tracker][i] = x_o

    elif the_game[board_tracker][2] == the_game[board_tracker][5] == the_game[board_tracker][8]:
        print(f"Tile {board_tracker + 1} has been taken!")
        for i in range(len(the_game)):
            the_game[board_tracker][i] = x_o           

def check_win(n):

    n = (n%2) + 1

    if all(element == "X" for element in the_game[0]) and all(element == "X" for element in the_game[1]) and all(element == "X" for element in the_game[2]):
        print(f"Player {n} wins!")
        show_entire_board()
        return 0

    elif all(element == "X" for element in the_game[3]) and all(element == "X" for element in the_game[4]) and all(element == "X" for element in the_game[5]):
        print(f"Player {n} wins!")
        show_entire_board()
        return 0
    
    elif all(element == "X" for element in the_game[6]) and all(element == "X" for element in the_game[7]) and all(element == "X" for element in the_game[8]):
        print(f"Player {n} wins!")
        show_entire_board()
        return 0
    
    elif all(element == "X" for element in the_game[0]) and all(element == "X" for element in the_game[3]) and all(element == "X" for element in the_game[6]):
        print(f"Player {n} wins!")
        show_entire_board()
        return 0
    
    elif all(element == "X" for element in the_game[1]) and all(element == "X" for element in the_game[4]) and all(element == "X" for element in the_game[7]):
        print(f"Player {n} wins!")
        show_entire_board()
        return 0   

    elif all(element == "X" for element in the_game[2]) and all(element == "X" for element in the_game[5]) and all(element == "X" for element in the_game[8]):
        print(f"Player {n} wins!")
        show_entire_board()
        return 0

    elif all(element == "X" for element in the_game[0]) and all(element == "X" for element in the_game[4]) and all(element == "X" for element in the_game[8]):
        print(f"Player {n} wins!")
        show_entire_board()
        return 0

    elif all(element == "X" for element in the_game[2]) and all(element == "X" for element in the_game[4]) and all(element == "X" for element in the_game[6]):
        print(f"Player {n} wins!")
        show_entire_board()
        return 0
    
# for O's


    elif all(element == "O" for element in the_game[0]) and all(element == "O" for element in the_game[1]) and all(element == "O" for element in the_game[2]):
        print(f"Player {n} wins!")
        show_entire_board()
        return 0

    elif all(element == "O" for element in the_game[3]) and all(element == "O" for element in the_game[4]) and all(element == "O" for element in the_game[5]):
        print(f"Player {n} wins!")
        show_entire_board()
        return 0
    
    elif all(element == "O" for element in the_game[6]) and all(element == "O" for element in the_game[7]) and all(element == "O" for element in the_game[8]):
        print(f"Player {n} wins!")
        show_entire_board()
        return 0
    
    elif all(element == "O" for element in the_game[0]) and all(element == "O" for element in the_game[3]) and all(element == "O" for element in the_game[6]):
        print(f"Player {n} wins!")
        show_entire_board()
        return 0
    
    elif all(element == "O" for element in the_game[1]) and all(element == "O" for element in the_game[4]) and all(element == "O" for element in the_game[7]):
        print(f"Player {n} wins!")
        show_entire_board()
        return 0   

    elif all(element == "O" for element in the_game[2]) and all(element == "O" for element in the_game[5]) and all(element == "O" for element in the_game[8]):
        print(f"Player {n} wins!")
        show_entire_board()
        return 0

    elif all(element == "O" for element in the_game[0]) and all(element == "O" for element in the_game[4]) and all(element == "O" for element in the_game[8]):
        print(f"Player {n} wins!")
        show_entire_board()
        return 0

    elif all(element == "O" for element in the_game[2]) and all(element == "O" for element in the_game[4]) and all(element == "O" for element in the_game[6]):
        print(f"Player {n} wins!")
        show_entire_board()
        return 0




game = True
n = 0
board_tracker = 4 # the board tracker tracks which board we are in (we start at 4, we start at the center always)
while game:

    show_entire_board()

    if all(element == "X" or element == "O" for element in the_game[board_tracker]):  # this statement ensures that the user picks a new tile when one is fully taken
        while all(element == "X" or element == "O" for element in the_game[board_tracker]):
            print("Choose a tile!")
            user = input()
            board_tracker = int(user) - 1
        show_entire_board()

    user = input()

    if user == 'q': # quit
        break

    spot = int(user) - 1 # forces player to next space

    if the_game[board_tracker][spot] == "X" or the_game[board_tracker][spot] == "O":
        while the_game[board_tracker][spot] == "X" or the_game[board_tracker][spot] == "O":
            print("Please choose a spot that is not taken")
            user = input()
            spot = int(user) - 1

        the_game[board_tracker][spot] = turn(n)
    else:
        the_game[board_tracker][spot] = turn(n)

    check_entire_tile(board_tracker,turn(n))

    board_tracker = spot # pushes board to that spot

    if check_win(n) == 0:
        print(f"Player {(n%2) + 1} wins!")
        break

    n = n+1
    
