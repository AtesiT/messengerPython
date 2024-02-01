from tkinter import *
from tkinter import ttk

def settings():
    settings = Tk()
    settings.title("Messenger")
    settings.geometry("350x600")

    title = ttk.Label(settings, text="Settings", font=("Century Gothic", 16))
    title.pack(pady=10)
    # title.grid(row=0, column=0)
    # title.place(relx=.4)


    # total settings of the buttons
    x = 7
    y = 7

    #BUTTONS
    btn1 = ttk.Button(settings, text="Экспортировать диалоги")
    btn1.pack(fill='x', expand=False, padx=x, pady=y, ipady=y)
    btn2 = ttk.Button(settings, text="Импортировать диалоги")
    btn2.pack(fill='x', expand=False, padx=x, pady=y, ipady=y)
    btn3 = ttk.Button(settings, text="Добавить сообщения в опеределённый диалог")
    btn3.pack(fill='x', expand=False, padx=x, pady=y, ipady=y)
    btn4 = ttk.Button(settings, text="Дублировать диалоги")
    btn4.pack(fill='x', expand=False, padx=x, pady=y, ipady=y)
    btn5 = ttk.Button(settings, text="Переключиться на другой аккаунт")
    btn5.pack(fill='x', expand=False, padx=x, pady=y, ipady=y)

    btn6 = ttk.Button(settings, text="Закрыть окно", command=lambda: settings.destroy())
    btn6.pack(fill='x', expand=False, padx=x, pady=y+50, ipady=y, anchor="center")


    settings.mainloop()

