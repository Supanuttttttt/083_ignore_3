from tkinter import *
import os
import tkinter as tk
from PIL import ImageTk,Image

root = Tk()
root.title('เกมสุ่มคำศัพท์')
root.geometry("600x500")
root.tk.call('wm','iconphoto',root._w,tk.PhotoImage(file='img111.png'))

def play():
    root.destroy()
    filename = 'wordgame.py'
    os.system(filename)

canva = Canvas(root,bg="black",height=500,width=600)
img12 = ImageTk.PhotoImage(Image.open("D:\Project Lab\kiminoto.png"))
canva.create_image(0,0,anchor=NW,image=img12)

button = Button(root, text="Start",command = play, font=("Helvetica", 30),width=8,height=1)
button.place(relx=0.5, rely=0.5, anchor=CENTER)

canva.pack()
root.mainloop()