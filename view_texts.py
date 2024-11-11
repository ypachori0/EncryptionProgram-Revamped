from tkinter import *
from tkinter import filedialog
import os

# create a window
window = Tk()
window.geometry("854x480")
window.title("View Encrypted Texts")

# add a label
label = Label(window,
text="",
font=("Helvetica", 12),
wraplength=800,
justify=LEFT)
label.pack(pady=10)

# display file contents to label
filepath = "cipher_texts.txt"
try:
    with open(filepath, 'r') as file:
        file_contents = file.read()
        label.config(text=file_contents) # print the contents of the file to the label
except FileNotFoundError:
    result_label.config(text="File not found")

window.mainloop()