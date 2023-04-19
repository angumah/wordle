from Model.board import Board
import tkinter as tk

class GameView():

    def __init__(self, board, root):
        """
        Constructor for GameView object whcih renders Wordle board.
        """
        self.board = board
        self.root = root
        self.root.geometry(f"{self.board.getRow()*40}x{self.board.getCol()*60}")
        self.root.title("PY-Wordle")


    def checkGuess(self, grid):
        """
        checks inputted guess against the actual word
        """

        charArr = [[None] * self.board.getCol() for _ in range(self.board.getRow())]
        cells = grid.children

        entryKeys = list(cells.keys())
        index = 0
        for i in range(self.board.getRow()):
            for j in range(self.board.getCol()):
                key = entryKeys[index]
                cell = cells[key]
                charArr[i][j] = cell.get()
                index += 1

        guess = ''.join(charArr[self.board.getGuessAttempt()])
        score = self.board.checkGuess(guess.lower())
        print(guess)
        print(score)
        self.renderRow(cells, score)
        self.board.takeAttempt()
        if self.board.endGame(guess):
            winWindow = tk.Tk()
            winWindow.geometry("150x200")
            winWindow.title("PY-Wordle")
            endFrame = tk.Frame(winWindow)
            endTitle = tk.Label(endFrame, text="Statistics", font=("Arial", 12))
            endTitle.pack()

            guesses = tk.Label(endFrame, text=f"Attempts : {self.board.getGuessAttempt()}")
            guesses.pack()
            endFrame.pack()

    def renderRow(self, children, score):
        """
        Re-renders board after a guess has been taken
        """
        attempt = self.board.getGuessAttempt()
        row = self.board.getCol()
        entryKeys = list(children.keys())

        for i in range(row):
            cell = children[entryKeys[(row*attempt)+i]]
            if score[i] == 0:
                continue
                #no need to modify
            elif score[i] == 1:
                cell.configure(background='#ebc249')
            elif score[i] == 2:
                cell.configure(background='#47ba32')





    def renderBoard(self):
        """
        Renders visual representation of wordle game board
        """
        titleFrame = tk.Frame(self.root)
        gameTitle = tk.Label(titleFrame, text="PY-Wordle", font=("Arial", 24))
        gameTitle.pack()
        gridFrame = tk.Frame(self.root)
        for i in range(self.board.getRow()):
            for j in range(self.board.getCol()):
                cell = tk.Entry(gridFrame, justify="center", width=2, font=("Arial", 24))
                cell.grid(row = i, column = j)

        buttonFrame = tk.Frame(self.root)

        submitButton = tk.Button(buttonFrame, text="Submit", font=("Arial", 16), justify="center", command=lambda: self.checkGuess(gridFrame))
        submitButton.pack()

        titleFrame.pack()
        gridFrame.pack()
        buttonFrame.pack()
        self.root.mainloop()


    