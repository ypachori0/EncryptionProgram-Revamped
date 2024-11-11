# encrypt.py
from tkinter import *
from tkinter import messagebox
import random
import string
import sys
import os
import utils # import the utils.py file

## generate the screen
# create the window
window = Tk()
window.geometry("854x480")
window.title("Encrypt a Message")

# add a label
label = Label(window,
text="Please enter the plain text",
font=('Helvetica', 24, 'bold'),
padx=10,
pady=10)
label.pack()

## prompt user for input
# entry widget
entry = Entry()
entry.config(font=("Helvetica", 12))
entry.config(width=25)
entry.place(x=100,y=100)

# submit button
submit_encrypt = Button(window,text="Submit", command=lambda: utils.submit_encrypt(entry, result_label))
submit_encrypt.place(x=320,y=100)

# label to show the cipher text
result_label = Label(window, text="", font=("Helvetica", 24, 'bold'), bg='gray', padx=10, pady=10)
result_label.place(x=100, y=300)

# dialog box asking if user wants to save cipher text to file
save_button = Button(window, text="Save text", command=lambda: utils.click_encrypt(result_label.cget("text"), window))
save_button.pack()


# run the program
window.mainloop()