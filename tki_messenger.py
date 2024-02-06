from tkinter import *
from tkinter import ttk
import settings_messenger
import profile_messenger
import createNewDialog_messenger

root = Tk()
root.title("Messenger")
root.geometry("340x600")


class AnyDialog:
    def __init__(self, name, text, time, numberLines):
        self.name = name
        self.text = text
        self.time = time
        self.numberLines = numberLines
        everyheightline = 0
        # print((lambda text: text[0:25] if len(text) > 25 else text)(text))
        if len(self.text) > 20:
            self.text = self.text[0:20] + '..'
        if len(self.name) > 7:
            self.name = self.name[0:7] + '..'
        for i in range(numberLines):
            name = ttk.Label(text=f"{self.name}", font=("Century Gothic", 10))
            name.place(x=10, y=50 + everyheightline)
            text = ttk.Label(text=f"{self.text}", font=("Century Gothic", 14))
            text.place(x=70, y=50 + everyheightline)
            time = ttk.Label(text=f"{str(self.time)}", font=("Century Gothic", 10))
            time.place(x=270, y=50 + everyheightline)
            everyheightline += 25

class UpperPartMesssenger:
    def __init__(self):
        settings = ttk.Button(text="Settings", command=settings_messenger.settings)
        settings.place(x=10, y=10)
        profile = ttk.Button(text="Profile", command=profile_messenger.profile)
        profile.place(x=250, y=10)

class BottomPartMesssenger:
    def __init__(self):
        ttk.Entry().place(x=10, y=500, height=40, width=220)
        ttk.Button(text='SEND').place(x=250, y=500, height=40)

class BottomToolbar:
    def __init__(self):
        settings = ttk.Button(text="MUSIC")
        settings.place(x=10, y=555)
        profile = ttk.Button(text="CREATE NEW DIALOG", command=createNewDialog_messenger.newDialog)
        profile.place(x=100, y=555)
        settings = ttk.Button(text="BACKUP")
        settings.place(x=250, y=555)



UpperPartMesssenger()
AnyDialog('Alice', 'Hi, How\'s going on?', '14:17', 15)
BottomPartMesssenger()
BottomToolbar()

root.mainloop()