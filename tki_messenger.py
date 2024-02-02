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
        name.grid(row=1,column=0)
        text = ttk.Label(text=f"{text}", font=("Century Gothic", 14))
        text.grid(row=1,column=1)
        time = ttk.Label(text=f"{str(time)}", font=("Century Gothic", 10))
        time.grid(row=1,column=2)

class UpperPartMesssenger:
    def __init__(self):
        settings = ttk.Button(text="Settings", command=settings_messenger.settings)
        settings.grid(row=0,column=0)
        profile = ttk.Button(text="Profile", command=profile_messenger.profile)
        profile.grid(row=0,column=2)

class BottomPartMesssenger:
    def __init__(self):
        ttk.Entry().grid(row=2,column=0, columnspan=2, stick='we')
        ttk.Button(text='SEND').grid(row=2,column=2)

class BottomToolbar:
    def __init__(self):
        settings = ttk.Button(text="MUSIC")
        settings.grid(row=3,column=0, stick='we')
        profile = ttk.Button(text="CREATE NEW DIALOG", command=createNewDialog_messenger.newDialog)
        profile.grid(row=3,column=1, stick='we')
        settings = ttk.Button(text="BACKUP")
        settings.grid(row=3,column=2, stick='we')



UpperPartMesssenger()
first_dialog = AnyDialog('Alice', 'Hi, How\'s going on?', '14:17')
BottomPartMesssenger()
BottomToolbar()

root.mainloop()