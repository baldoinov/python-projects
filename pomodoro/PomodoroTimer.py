from tkinter import ttk
import tkinter as tk
import threading
import time
 
class Pomodoro(tk.Tk):

    def __init__(self) -> None:
        super().__init__()

        self.title('Pomodoro Timer')
        self.geometry('300x200')
        self.resizable(False, False)


if __name__ == '__main__':
    app = Pomodoro()
    app.mainloop()