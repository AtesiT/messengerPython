from tkinter import *
from tkinter import ttk
from tkinter.messagebox import OK, INFO, showinfo
import random

def profile():
    profile = Tk()
    profile.title("Messenger")
    profile.geometry("350x600")

    createRandomKey = lambda: int(round(random.random(), 10) * 10000000000)

    def takeKey():
        showinfo(title="Messenger",
                 message="Ключ для установления связи с новым собеседником будет доступен в течении минуты",
                 detail=f"Отправьте собеседнику для создания диалога с ним: {(createRandomKey())}",
                 icon=INFO, default=OK)

    title = ttk.Label(profile, text="Your profile", font=("Century Gothic", 16))
    title.pack(pady=10)
    btnCreateKey = ttk.Button(profile, text="Создать ключ для соеденинения с новым собеседником", command=takeKey)
    btnCreateKey.pack(fill='x', expand=False, padx=5, pady=5, ipady=5,)

    btnClose = ttk.Button(profile, text="Закрыть окно", command=lambda: profile.destroy())
    btnClose.pack(fill='x', expand=False, padx=5, pady=50, ipady=5, anchor="center")