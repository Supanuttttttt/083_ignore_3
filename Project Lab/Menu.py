from tkinter import *
import os
import tkinter as tk
from PIL import ImageTk,Image

root = Tk()

def play():
    root.destroy()
    filename = 'connect4_with_ai.py'
    os.system(filename)

def play1():
    root.destroy()
    filename = 'connect4.py'
    os.system(filename)    

root.title('บิงโกเรียง 4')
root.geometry("600x400")
root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='P1.png'))

c = Canvas(root,bg="black",height=400,width=600)
img = ImageTk.PhotoImage(Image.open("D:\Project Lab\Testting.png"))
c.create_image(0,0,anchor=NW,image=img)

button = Button(root, text="Player Vs Bot",command = play, font=("Helvetica", 24))
button.place(relx=0.5, rely=0.5, anchor=CENTER)

button1 = Button(root, text="Player Vs Player",command = play1, font=("Helvetica", 24))
button1.place(x = 170 , y = 250)

c.pack()
root.mainloop()