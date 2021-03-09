#!/usr/bin/env/python3
"""script for git use"""

import tkinter as tk
import os

app1 = tk.Tk()
app1.title("GitUpload | by Wh04m1Su")
app1.geometry("420x430")

app1.config(bg = '#fff')
app1.resizable(False, False)

imghot=tk.PhotoImage(file="images/git.png")
tk.Label(app1, image=imghot, bg = '#fff').place(x = 90, y = 5)


def addfile():
    """for add new file to git"""

    add = entry2l.get()
    os.system('cd temp ; git add ' + add)
    os.system('cd temp ; git status')


def upinfo():
    """ for upload the local git to github or similar """
    remurl = entry3l.get()
    com = entry1l.get()
    os.system('cd temp ; git init')
    os.system('cd temp ; git commit -m ' + com)
    os.system('cd temp ; git remote add origin ' + remurl)
    os.system('cd temp ; git push -u origin master')
    uplabel.place(x = 10, y = 405)


#entry vars
entry1l = tk.StringVar()
entry1 = tk.Entry(app1, textvariable=entry1l, fg = '#343434', bg = '#fff')
entry1.place(x = 200, y = 280)

entry2l = tk.StringVar()
entry2 = tk.Entry(app1, textvariable=entry2l, fg = '#343434', bg = '#fff')
entry2.place(x = 200, y = 250)

entry3l = tk.StringVar()
entry3 = tk.Entry(app1, textvariable=entry3l, fg = '#343434', bg = '#fff')
entry3.place(x = 200, y = 320)


#section for labels and buttons
uplabel = tk.Label(app1, text='!!TYPE IN CONSOL USR AND PASS OF GITHUB!!')
uplabel.config(bg = '#fff', font =(15), fg = '#7BA8FF')

tk.Label(app1, font =(20), text='Enter Commit: ', fg = '#343434', bg = '#fff').place(x = 9, y = 280)

tk.Label(app1, font =(20), text='File to ADD: ', fg = '#343434', bg = '#fff').place(x = 9, y = 250)

tk.Label(app1, font =(20), text='Enter Remote Url: ', fg = '#343434', bg = '#fff').place(x = 9, y = 320)

bottonadd = tk.Button(app1, text = 'add', bg = '#39394A', fg = '#7BA8FF', command=addfile)
bottonadd.place(x = 369, y = 245)

bottonupload = tk.Button(app1, text = 'Upload', bg = '#39394A', fg = '#7BA8FF', command=upinfo)
bottonupload.place(x = 160, y = 370)

app1.mainloop()
