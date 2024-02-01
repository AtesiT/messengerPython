from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Messenger")
root.geometry("360x640")

class AnyDialog:
    def __init__(self, name, text, time):
        name = ttk.Label(text=f"{name}", font=("Century Gothic", 10))
        name.pack()
        text = ttk.Label(text=f"{text}", font=("Century Gothic", 14))
        text.pack()
        time = ttk.Label(text=f"{str(time)}", font=("Century Gothic", 10))
        time.pack()

class UpperPartMesssenger:
    pass

class BottomPartMesssenger:
    pass


first_dialog = AnyDialog('Alice', 'Hi, How\'s going on?', 20)
root.mainloop()