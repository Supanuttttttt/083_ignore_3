from tkinter import *
import os
import tkinter as tk
from PIL import ImageTk,Image

root = Tk()

def play():
    root.destroy()
    filename = 'real02.py'
    os.system(filename)

root.title('Checkers')
root.geometry("600x400")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='P2.png'))

c = Canvas(root,bg="black",height=400,width=600)
img = ImageTk.PhotoImage(Image.open("D:\Project Lab\Asdqweq.png"))
c.create_image(0,0,anchor=NW,image=img)

button1 = Button(root, text="Start",command = play, font=("Helvetica", 24),bg='#8B4513')
button1.place(x = 250 , y = 200)

c.pack()
root.mainloop()