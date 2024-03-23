from tkinter import messagebox

import ttkbootstrap as ttk


class Application(ttk.Window):
    def __init__(self) -> None:
        super().__init__(themename="darkly", size=(500, 500), hdpi=False)
        self.title("Tic Tac Toe")

        self.columnconfigure((0, 1, 2), weight=1)
        self.rowconfigure((0, 1, 2), weight=1)

        self.player_x = {"text": "❌", "bootstyle": "success"}
        self.player_o = {"text": "⭕️", "bootstyle": "danger"}
        self.prev_player = None

        self.buttons = dict()
        for column in range(3):
            for row in range(3):
                coord = (column, row)
                self.button = ttk.Button(
                    self,
                    text="",
                    command=lambda coord=coord: self.on_choice(coord),
                    takefocus=False,
                )
                self.button.grid(row=row, column=column, padx=(2, 2), pady=(2, 2), sticky="nsew")
                self.buttons[coord] = self.button

    def on_choice(self, coord: tuple) -> None:
        if self.buttons[coord]["text"] == "":
            player = self.player_o
            if self.prev_player is None or self.prev_player == self.player_o:
                player = self.player_x

            self.buttons[coord].configure(**player)
            winner = self.check_winner()
            if winner:
                messagebox.showinfo("Игра окончена", f"{winner} победил!")
                self.reset_board()
            elif all(btn["text"] != "" for btn in self.buttons.values()):
                messagebox.showinfo("Игра окончена", "Ничья!")
                self.reset_board()
            else:
                self.prev_player = player

    def check_winner(self) -> str:
        board = [[self.buttons[(x, y)]["text"] for y in range(3)] for x in range(3)]
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] != "":
                return board[i][0]
            if board[0][i] == board[1][i] == board[2][i] != "":
                return board[0][i]

        if board[0][0] == board[1][1] == board[2][2] != "":
            return board[0][0]
        if board[0][2] == board[1][1] == board[2][0] != "":
            return board[0][2]
        return ""

    def reset_board(self) -> None:
        [btn.configure(text="", bootstyle="primary") for btn in self.buttons.values()]
        self.prev_player = None


app = Application()
app.mainloop()
