from tkinter import *
from tkinter import ttk

def newDialog():
    newDialog = Tk()
    newDialog.title("Messenger")
    newDialog.geometry("350x600")

    textPutKey = ttk.Label(newDialog, text="Введите ключ для создания диалога с новым собеседником")
    textPutKey.pack( padx=6, pady=6)

    putKey = ttk.Entry(newDialog)
    putKey.pack( padx=6, pady=6)

    enterKey = ttk.Button(newDialog, text="Ввести ключ", command=lambda: newDialog.destroy())
    enterKey.pack( padx=6, pady=6)
