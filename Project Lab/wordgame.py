from random import choice
from random import shuffle
from tkinter import *
import tkinter as tk
import os

windowWord = Tk()
windowWord.title('เกมสุ่มคำศัพท์')
windowWord.geometry("600x500")
windowWord.configure(bg='White')
windowWord.tk.call('wm','iconphoto',windowWord._w,tk.PhotoImage(file='img111.png'))

my_label = Label(windowWord, text="", font=("Helvetica", 48),bg='White')
my_label.pack(pady=20)

score = 0
def shuffler():
    # Clear Hint Label 
    hint_label.config(text='',bg='White')

    # Clear Hint Count
    global hint_count
    hint_count = 0

    # Clear Answer Box
    entry_answer.delete(0, END)

    # Clear Answer Label
    answer_label.config(text='',bg='White')

    # List of state words
    states = ['Cat', 'Elephant', 'Duck', 'Hippopotamus', 'Boar', 'Shell', 'Gibbon', 'Apple', 'Banana', 'Pear', 'Melon', 'Carrot', 'Garlic', 'Tomato', 'Seaweed'
    , 'Pepper', 'Taro', 'Bamboo Shoot', 'Spring Onion', 'Pink', 'Green', 'White', 'Gold', 'Purple', 'Bronze', 'Cyan', 'Blue', 'Monday', 'Tuesday', 'Wednesday'
    , 'Thursday', 'Friday', 'Saturday', 'Sunday', 'January', 'Febuary', 'March', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    # Pick random state from list
    global word
    word = choice(states)
    

    # Break apart our chosen word
    break_apart_word = list(word)
    shuffle(break_apart_word)
    
    # Turn shuffeled List into a word
    global shuffled_word
    shuffled_word =  ''
    for letter in break_apart_word:
        shuffled_word += letter
    
    # print shuffled word to the screen
    my_label.config(text=shuffled_word,bg='White')

#Create answer Function
def answer():
    global score
    if word == entry_answer.get():
        score += 1
        answer_label.config(text="ถูกต้อง!!!")
        score_label.config(text=score,bg='White')
    else:
        score = score-1
        answer_label.config(text="ผิดดดดด!!!")
        score_label.config(text=score)
    shuffler()


# Create Hint Counter
global hint_count
hint_count = 0

# Create Hint Function
def hint(count):
    global hint_count
    hint_count = count
    global score
    # Get the length of the chosen word
    word_length = len(word)

    # Show Hint
    if count < word_length:
        score = score-1
        score_label.config(text=score)
        hint_label.config(text=f'{hint_label["text"]} {word[count]}')
        hint_count +=1 

def backmenu():
    windowWord.destroy()
    filename = 'menu0.py'
    os.system(filename)

score_label = Label(windowWord, text='', font=("Helvetica", 18),bg='White')
score_label.pack(padx= 10)

entry_answer = Entry(windowWord, font=("Helvetica", 24),bg='White')
entry_answer.pack(pady=20)


button_frame = Frame(windowWord,bg='White')
button_frame.pack(pady=20)

answer_button = Button(button_frame, text="ยืนยันคำตอบ", command=answer,bg='White')
answer_button.grid(row=0, column=0, padx=10)

hint_button = Button(button_frame, text="ใบ้คำ",bg='White', command=lambda: hint(hint_count))
hint_button.grid(row=0, column=2, padx=10)

answer_label = Label(windowWord, text='', font=("Helvetica", 18),bg='White')
answer_label.pack(pady=20)

hint_label = Label(windowWord, text='', font=("Helvetica", 18),bg='White')
hint_label.pack(pady=10)

back_button = Button(button_frame, text="กลับหน้าหลัก",bg='White', command=backmenu)
back_button.grid(row=0, column=4, padx=10)

shuffler()
windowWord.mainloop()