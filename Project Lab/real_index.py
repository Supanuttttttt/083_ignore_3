import tkinter as tk
from tkinter import *
import os

#-------------------------------def
def game_1(): #เกมใบ้คำ
    filename = 'menu0.py'
    os.system(filename)

def game_2(): #เกมบิงโก
    filename = 'Menu.py'
    os.system(filename)

def game_3(): #เกมซูโดกุ
    filename = 'Menu1.py'
    os.system(filename)

def game_4(): #เกมงู
    filename = 'Menu4.py'
    os.system(filename)

def game_5(): #เกมหมากฮอส
    filename = 'Menu2.py'
    os.system(filename)

#-------------------------------label
win = Tk()
win.title("MINIGAMES")
win.geometry("1200x1200")
win.tk.call('wm','iconphoto',win._w,PhotoImage(file='unnamed1.png'))
win.configure(bg="#FE8D6F")

L_0 = Label(win,text="MINIGAMES",font=("Comic Sans MS",64),bg="#FE8D6F",fg="white")
L_0.place(x=320,y=50)

def on_hover(button, colorOnHover, colorOnLeave):
	button.bind("<Enter>", func=lambda e: button.config(background="#A0DDE0",foreground=colorOnHover))
	button.bind("<Leave>", func=lambda e: button.config(background="#A0DDE0",foreground=colorOnLeave))

b_1 = Button(win,text="WORD GUESS",command=game_1,font=("Comic Sans MS",24),bg="#A0DDE0",fg="black",activebackground="#789CCE",activeforeground="white")
b_1.place(x=200,y=200,height=150,width=250)
on_hover(b_1,"white","black")

b_2 = Button(win,text="BINGO",command=game_2,font=("Comic Sans MS",24),bg="#A0DDE0",fg="black",activebackground="#789CCE",activeforeground="white") 
b_2.place(x=200,y=400,height=150,width=250)
on_hover(b_2,"white","black")

b_3 = Button(win,text="SUDOKU",command=game_3,font=("Comic Sans MS",24),bg="#A0DDE0",fg="black",activebackground="#789CCE",activeforeground="white") 
b_3.place(x=470,y=600,height=150,width=250)
on_hover(b_3,"white","black")

b_4 = Button(win,text="SNAKE",command=game_4,font=("Comic Sans MS",24),bg="#A0DDE0",fg="black",activebackground="#789CCE",activeforeground="white") 
b_4.place(x=750,y=200,height=150,width=250)
on_hover(b_4,"white","black")

b_5 = Button(win,text="CHECKERS",command=game_5,font=("Comic Sans MS",24),bg="#A0DDE0",fg="black",activebackground="#789CCE",activeforeground="white")
b_5.place(x=750,y=400,height=150,width=250)
on_hover(b_5,"white","black")

win.mainloop()