from View.gameView import GameView

from Model.board import Board

from Model.randWord import RandWord

from Controller.wordle import Wordle

import tkinter as tk

# root = tk.Tk()

# def renderStart():
#         root.title("Wordle")
#         root.geometry("500x500")

#         # logo = tk.PhotoImage(file="logo.png")

#         title_label = tk.Label(root, text="Welcome to Wordle!", font=("Arial", 24))
#         title_label.pack(pady=20)


#         start_button = tk.Button(root, text="Start", font=("Arial", 16), command=selectDifficulty)
#         start_button.pack(pady=20)

#         root.mainloop()


# def selectDifficulty():
#         root.geometry("500x500")

#         title_label = tk.Label(root, text="Select Gamemode", font=("Arial", 24))
#         title_label.pack(pady=20)


#         easy_button = tk.Button(root, text="Easy", font=("Arial", 16), command=setGame(5))
#         easy_button.pack(pady=20)
#         easy_label = tk.Label(root, text="5-letter word", font=("Arial", 24))
#         easy_label.pack(pady=20)

#         medium_Button = tk.Button(root, text="Medium", font=("Arial", 16), command=setGame(6))
#         medium_Button.pack(pady=20)
#         medium_label = tk.Label(root, text="6-letter word", font=("Arial", 24))
#         medium_label.pack(pady=20)

#         hard_Button = tk.Button(root, text="Hard", font=("Arial", 16), command=setGame(7))
#         hard_Button.pack(pady=20)
#         hard_label = tk.Label(root, text="7-letter word", font=("Arial", 24))
#         hard_label.pack(pady=20)

#         root.mainloop()

# def setGame(size):
#         print(size)
        

gb = Board(5)
gv = GameView(gb, tk.Tk())


controller = Wordle(gb, gv)
controller.run()


