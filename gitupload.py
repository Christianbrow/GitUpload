#!/usr/bin/env/python3

###################################################
# Createby: wh04m1su
# Gmail: wh04m1su@gmail.com
# Telegram: https://t.me/wh04m1su 

from tkinter.ttk import *
from tkinter import PhotoImage
from tkinter import filedialog
import tkinter as tk
import os 
import sys

app = tk.Tk()
app.title("GitUpload | by Wh04m1Su")
app.geometry("400x330")
app.config(bg = '#fff')


progress = Progressbar(app, orient = 'horizontal', length = 390, mode = 'determinate')
img=tk.PhotoImage(file="images/gith.png")
labelfont = tk.Label(app, image=img, bg = '#fff').place(x = 90, y = 5)




def Program():

	os.system('python3 modulos/programn.py')


def bar(): 

    import time 

    progress['value'] = 0
    app.update_idletasks() 
    time.sleep(1)

    progress['value'] = 10
    app.update_idletasks() 
    time.sleep(1)
    
    progress['value'] = 20
    app.update_idletasks() 
    time.sleep(1)
    
    progress['value'] = 30
    app.update_idletasks() 
    time.sleep(1)

    progress['value'] = 40
    app.update_idletasks() 
    time.sleep(1) 
  
    progress['value'] = 50
    app.update_idletasks() 
    time.sleep(1) 
  
    progress['value'] = 60
    app.update_idletasks() 
    time.sleep(1) 
  
    progress['value'] = 70
    app.update_idletasks() 
    time.sleep(1) 
  
    progress['value'] = 80
    app.update_idletasks() 
    time.sleep(1) 
    progress['value'] = 90
    
    progress['value'] = 100
    app.update_idletasks() 
    time.sleep(1)

    

progress.place(x = 5, y = 260)

labelmen = tk.Label(app, text = 'Welcome to GitUpload for wh04m1su ..', font = (20), fg = '#343434', bg = '#fff').place(x = 34, y = 290)

bar()


Program()


app.mainloop()