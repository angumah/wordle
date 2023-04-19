from View.setDifficulty import SetDifficulty


import tkinter as tk

root = tk.Tk()
root.title("Wordle")
root.geometry("500x500")
def renderStart():
    # logo = tk.PhotoImage(file="logo.png")

    title_label = tk.Label(root, text="Welcome to Wordle!", font=("Arial", 24))
    title_label.pack(pady=20)


    start_button = tk.Button(root, text="Start", font=("Arial", 16), command= setDiff)
    start_button.pack(pady=20)
    root.mainloop()


def setDiff():
    root.destroy()
    sd = SetDifficulty(tk.Tk())
    sd.setDifficulty()

renderStart()
