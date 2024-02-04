from tkinter import *
from tkinter import ttk
import settings_messenger
import profile_messenger
import createNewDialog_messenger

root = Tk()
root.title("Messenger")
root.geometry("350x600")

class AnyDialog:
    def __init__(self, name, text, time):
        name = ttk.Label(text=f"{name}", font=("Century Gothic", 10))
        name.place(x=10, y=50)
        text = ttk.Label(text=f"{text}", font=("Century Gothic", 14))
        text.place(x=70, y=50)
        time = ttk.Label(text=f"{str(time)}", font=("Century Gothic", 10))
        time.place(x=270, y=50)

class UpperPartMesssenger:
    def __init__(self):
        settings = ttk.Button(text="Settings", command=settings_messenger.settings)
        settings.place(x=10, y=10)
        profile = ttk.Button(text="Profile", command=profile_messenger.profile)
        profile.place(x=250, y=10)

class BottomPartMesssenger:
    def __init__(self):
        ttk.Entry().place(x=10, y=500)
        ttk.Button(text='SEND').place(x=250, y=500)

class BottomToolbar:
    def __init__(self):
        settings = ttk.Button(text="MUSIC")
        settings.place(x=10, y=550)
        profile = ttk.Button(text="CREATE NEW DIALOG", command=createNewDialog_messenger.newDialog)
        profile.place(x=100, y=550)
        settings = ttk.Button(text="BACKUP")
        settings.place(x=250, y=550)



UpperPartMesssenger()
AnyDialog('Alice', 'Hi, How\'s going on?', '14:17')
BottomPartMesssenger()
BottomToolbar()

root.mainloop()