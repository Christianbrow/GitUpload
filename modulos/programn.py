#!/usr/bin/env/python3

import tkinter as tk
import os
import sys

app1 = tk.Tk()
app1.title("GitUpload | by Wh04m1Su")
app1.geometry("420x430")
app1.config(bg = '#fff')


imghot=tk.PhotoImage(file="images/git.png")
labelfonts = tk.Label(app1, image=imghot, bg = '#fff').place(x = 90, y = 5)


def addfile():
	add = entry2l.get()
	os.system('cd temp ; git add ' + add)
	os.system('cd temp ; git status')
	

def upinfo():
	add = entry2l.get()
	remurl = entry3l.get()
	com = entry1l.get()
	os.system('cd temp ; git init')
	os.system('cd temp ; git commit -m ' + com)
	os.system('cd temp ; git remote add origin ' + remurl)
	os.system('cd temp ; git push -u origin master')
	label4 = tk.Label(app1, text='!!TYPE IN CONSOL USR AND PASS OF GITHUB!!', bg = '#fff', font =(15), fg = '#7BA8FF').place(x = 10, y = 405)


entry1l = tk.StringVar()
entry1 = tk.Entry(app1, textvariable=entry1l, fg = '#343434', bg = '#fff').place(x = 200, y = 280)

entry2l = tk.StringVar()
entry2 = tk.Entry(app1, textvariable=entry2l, fg = '#343434', bg = '#fff').place(x = 200, y = 250)

entry3l = tk.StringVar()
entry3 = tk.Entry(app1, textvariable=entry3l, fg = '#343434', bg = '#fff').place(x = 200, y = 320)


label1 = tk.Label(app1, font =(20), text='Enter Commit: ', fg = '#343434', bg = '#fff').place(x = 9, y = 280)

label2 = tk.Label(app1, font =(20), text='File to ADD: ', fg = '#343434', bg = '#fff').place(x = 9, y = 250)

label3 = tk.Label(app1, font =(20), text='Enter the Remote Url: ', fg = '#343434', bg = '#fff').place(x = 9, y = 320)

bottonadd = tk.Button(app1, text = 'add', bg = '#39394A', fg = '#7BA8FF', command=addfile).place(x = 369, y = 245)

bottonupload = tk.Button(app1, text = 'Upload', bg = '#39394A', fg = '#7BA8FF', command=upinfo).place(x = 160, y = 370)


app1.mainloop()