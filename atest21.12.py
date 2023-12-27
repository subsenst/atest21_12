# С помощью библиотеки tkinter разработать интерфейс для своего приложения и собрать исполняемый файл в exe

# Импортируем нужные библиотеки
import tkinter as tk
from tkinter import BOTH, YES, LEFT, CENTER
from tkinter import ttk

# Создаём первичное окно запуска
window = tk.Tk()
window.geometry("490x500")

# Создаём кнопку запуска
button = tk.Button()
ttk.Button(text="Запуск сапёра",
           command=window.destroy).pack(anchor="center", expand=YES, fill=BOTH, padx=10, pady=75)

# Создаём кнопку поддержки разработчика
buttonS = tk.Button(text='поддержать разработчика')
buttonS.pack(anchor="s", expand=YES, fill=BOTH, padx=10, pady=75)

# Запуск
window.mainloop()


# Создаём вторичное окно с самим сапёром
windowGame = tk.Tk()
windowGame.title("Сапёр")
windowGame.geometry("490x500")

# Создаём нужные нам параметры
frame = []
button1 = []  # Спискок фреймов и кнопок
playArea = []
nMoves = 0

for i in range(0, 8):
    frame.append(tk.Frame())
    frame[i].pack(expand=YES, fill=BOTH)
    for j in range(0, 8):
        button1.append(tk.Button(frame[i], text=' ',
                                 font=('mono', 8, 'bold'),
                                 width=2, height=1, ))
        button1[i * 8 + j].pack(side=LEFT, expand=YES, fill=BOTH)

windowGame.mainloop()
