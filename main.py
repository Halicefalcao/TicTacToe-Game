import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.turn = 'X'
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_board()

    def create_board(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(
                    self.window,
                    text="",
                    font=("Times New Roman", 24),
                    height=2,
                    width=5,
                    command=lambda row=i, col=j: self.on_click(row, col)
                )
                self.buttons[i][j].grid(row=i, column=j)

    def on_click(self, row, col):
        if self.board[row][col] == '' and not self.check_winner():
            self.board[row][col] = self.turn
            self.buttons[row][col].config(text=self.turn)

            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.turn} wins!")
                self.reset_board()
            elif self.is_tie():
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_board()
            else:
                self.turn = 'O' if self.turn == 'X' else 'X'

    def check_winner(self):
        for row in self.board:
            if row[0] == row[1] == row[2] != '':
                return True
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != '':
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != '':
            return True
        return False

    def is_tie(self):
        for row in self.board:
            if '' in row:
                return False
        return True

    def reset_board(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j] = ''
                self.buttons[i][j].config(text="")
        self.turn = 'X'

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    game = TicTacToe()
    game.run()
