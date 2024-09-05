import tkinter as tk
from tkinter import messagebox

# finished version of super tic tac toe

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

class SuperTicTacToeUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Super Tic-Tac-Toe")
        self.n = 0
        self.board_tracker = 4  # start at center
        self.buttons = [[[] for _ in range(9)] for _ in range(9)]
        self.create_game_board()

    def turn(self, n):
        x_o = n % 2
        return 'X' if x_o == 0 else 'O'

    def handle_click(self, big_board, small_board):
        if self.board_tracker != -1 and big_board != self.board_tracker and not all(isinstance(x, str) for x in the_game[self.board_tracker]):
            messagebox.showerror("Invalid Move", f"You must play in board {self.board_tracker + 1}")
            return

        if isinstance(the_game[big_board][small_board], str):
            messagebox.showerror("Invalid Move", "This spot is already taken!")
            return

        current_player = self.turn(self.n)
        the_game[big_board][small_board] = current_player
        self.buttons[big_board][small_board].config(text=current_player, state="disabled")

        self.check_entire_tile(big_board, current_player)
        if self.check_win(self.n) == 0:
            self.root.quit()
            return

        self.board_tracker = small_board
        self.n += 1

        if all(isinstance(x, str) for x in the_game[self.board_tracker]):
            messagebox.showinfo("Board Full", f"Board {self.board_tracker + 1} is full. You can now play in any available board.")
            self.board_tracker = -1

        self.update_board_states()

    def check_entire_tile(self, board_tracker, x_o):
        win_conditions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8), 
            (0, 3, 6), (1, 4, 7), (2, 5, 8), 
            (0, 4, 8), (2, 4, 6) 
        ]

        for condition in win_conditions:
            if all(the_game[board_tracker][i] == x_o for i in condition):
                messagebox.showinfo("Board Taken", f"Tile {board_tracker + 1} has been taken by {x_o}!")
                for i in range(9):
                    the_game[board_tracker][i] = x_o
                    self.buttons[board_tracker][i].config(text=x_o, state="disabled")
                break

    def check_win(self, n):
        n = (n % 2) + 1
        win_conditions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6) 
        ]

        for player in ['X', 'O']:
            for condition in win_conditions:
                if all(all(element == player for element in the_game[i]) for i in condition):
                    messagebox.showinfo("Game Over", f"Player {n} ({player}) wins!")
                    return 0

        return 1

    def update_board_states(self):
        for big_board in range(9):
            if big_board == self.board_tracker or self.board_tracker == -1:
                for small_board in range(9):
                    if not isinstance(the_game[big_board][small_board], str):
                        self.buttons[big_board][small_board].config(state="normal")
                    else:
                        self.buttons[big_board][small_board].config(state="disabled")
            else:
                for small_board in range(9):
                    self.buttons[big_board][small_board].config(state="disabled")

    def create_game_board(self):
        for big_row in range(3):
            for big_col in range(3):
                big_board = big_row * 3 + big_col
                board_frame = tk.Frame(self.root, bd=5, relief="solid")
                board_frame.grid(row=big_row, column=big_col, padx=5, pady=5)

                for small_row in range(3):
                    for small_col in range(3):
                        small_board = small_row * 3 + small_col
                        button = tk.Button(board_frame, text=str(the_game[big_board][small_board]), 
                                           width=3, height=1, font=("Helvetica", 20),
                                           command=lambda br=big_board, sr=small_board: self.handle_click(br, sr))
                        button.grid(row=small_row, column=small_col, padx=1, pady=1)
                        self.buttons[big_board][small_board] = button

        self.update_board_states()

if __name__ == "__main__":
    root = tk.Tk()
    game = SuperTicTacToeUI(root)
    root.mainloop()