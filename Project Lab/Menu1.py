from tkinter import *
import os
import tkinter as tk
from PIL import ImageTk,Image

root = Tk()

def play():
    root.destroy()
    filename = 'real01.py'
    os.system(filename)

root.title('SUDOKU')
root.geometry("600x500")
root.tk.call('wm','iconphoto',root._w,tk.PhotoImage(file='asdd.png'))

canva = Canvas(root,bg="white",height=500,width=600)
img12 = ImageTk.PhotoImage(Image.open("D:\Project Lab\wegew.png"))
canva.create_image(0,0,anchor=NW,image=img12)

button = Button(root, text="Start",command = play, font=("Helvetica", 30),width=8,height=1)
button.place(relx=0.5, rely=0.5, anchor=CENTER)

canva.pack()
root.mainloop()