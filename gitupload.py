#!/usr/bin/env/python3

"""
 Createby: wh04m1su
 Gmail: wh04m1su@gmail.com
 Telegram: https://t.me/wh04m1su
 optimized by: https://www.github.com/N3koSempai
"""
from tkinter.ttk import Progressbar
from tkinter import PhotoImage
import tkinter as tk
import os
import time

app = tk.Tk()
app.title("GitUpload | by Wh04m1Su")
app.geometry("400x330")
app.config(bg = '#fff')
app.resizable(False, False)

img=PhotoImage(file="images/gith.png")
labelfont = tk.Label(app, image=img, bg = '#fff')
labelfont.place(x = 90, y = 5)
labelmen = tk.Label(app, text = 'Welcome to GitUpload for wh04m1su ..',)
labelmen.config(font = (20), fg = '#343434', bg = '#fff')
labelmen.place(x = 34, y = 290)
progress = Progressbar(app, orient = 'horizontal', length = 390, mode = 'determinate')




progress.place(x = 5, y = 260)


def pbar():
    """simple progressbar"""

    for i in range(10, 101,10):
        progress['value'] = i
        app.update_idletasks()
        time.sleep(1)

def program():
    """call to the second screen"""

    os.system('python3 modulos/programn.py')

pbar()

program()

app.mainloop()
