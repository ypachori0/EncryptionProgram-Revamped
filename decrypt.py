# decrypt.py
from tkinter import *
from tkinter import messagebox
import random
import string
import sys
import os

# function to submit text
def submit():
    global cipher_text
    plain_text = entry.get()
    cipher_text = "" # reset the variable each time submit button is pressed

    # iteratae over every letter in plain text
    for letter in plain_text:
        i = chars.index(letter)
        cipher_text += key[i]

    # update result label
    result_label.config(text=f"Cipher Text: {cipher_text}")

# window
window = Tk() # create the window
window.geometry("854x480") # set window size
window.title("Decrypt a message") # set window title

# use a label to show where to enter the cipher text
label = Label(window,
text="Please enter the cipher text:",
font=("Helvetica", 18, 'bold'))
label.place(x=25,y=100)

# use entry box to collect user input, submit button will be pressed
entry = Entry()
entry.config(font=("Helvetica", 12))
entry.config(width=25)
entry.config(background="gray")
entry.place(x=350,y=100)


# run the program
window.mainloop()