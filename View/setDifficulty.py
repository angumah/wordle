from Model.board import Board
import tkinter as tk
from View.gameView import GameView
from Model.board import Board
from Controller.wordle import Wordle

class SetDifficulty():
    def __init__(self, root):
        self.root = root
        self.root.geometry("500x500")
        self.root.title("Select Gamemode")

    def setDifficulty(self):
        title_label = tk.Label(self.root, text="Select Gamemode", font=("Arial", 24))
        title_label.pack(pady=20)


        easy_button = tk.Button(self.root, text="Easy", font=("Arial", 16), command=lambda: self.setGame(5))
        easy_button.pack(pady=20)
        easy_label = tk.Label(self.root, text="5-letter word", font=("Arial", 24))
        easy_label.pack(pady=20)

        medium_Button = tk.Button(self.root, text="Medium", font=("Arial", 16), command=lambda: self.setGame(6))
        medium_Button.pack(pady=20)
        medium_label = tk.Label(self.root, text="6-letter word", font=("Arial", 24))
        medium_label.pack(pady=20)

        hard_Button = tk.Button(self.root, text="Hard", font=("Arial", 16), command=lambda: self.setGame(7))
        hard_Button.pack(pady=20)
        hard_label = tk.Label(self.root, text="7-letter word", font=("Arial", 24))
        hard_label.pack(pady=20)

        self.root.mainloop()

    
    def setGame(self, size):
        self.root.destroy()
        gb = Board(size)
        gv = GameView(gb, tk.Tk())
        controller = Wordle(gb, gv)

        controller.run()

