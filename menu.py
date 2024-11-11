# menu.py
from tkinter import *
import os

# function to open the encryptor
def open_encrypt():
    window.destroy() # close the menu window
    os.system("python3 encrypt.py") # opens encrypt.py

# function to open the decryptor
def open_decrypt():
    window.destroy() # close the menu window
    os.system("python3 decrypt.py") # opens decrypt.py

# function to view encrypted texts
def open_view_texts():
    window.destroy() # close the menu window
    os.system("python3 view_texts.py") # opens file where encrypted texts are stored

# function to view list of characters
def open_chars():
    window.destroy() # close the menu window
    os.system("python3 chars.py") # open chars.py

# function to view the key
def open_key():
    window.destroy() # close the menu window
    os.system("python3 key.py") # open key.py

# function to exit
def open_exit():
    window.destroy() # close the main menu, exit program

# initialize the window
window = Tk()
window.geometry("854x480")
window.title("Main Menu")

# add the label
label = Label(window,
text="Main Menu",
font=("Helvetica", 24, 'bold'),
padx=10,
pady=10)
label.pack()

# initialize the frame
frame = Frame(window)
frame.pack()

# buttons
buttons = [
    ("Encrypt a\nMessage", 0, 0, open_encrypt),
    ("Decrypt a\nMessage", 0, 1, open_decrypt),
    ("View\nEncrypted\nTexts", 0 , 2, open_view_texts),
    ("View List\nof\nCharacters", 1, 0, open_chars),
    ("View\nKey", 1, 1, open_key),
    ("Exit", 1, 2, open_exit),
]

for (text, row, col, command) in buttons:
    Button(frame, text=text, font=("Helvetica", 12), width=10, height=10, command=command).grid(row=row, column=col, padx=5, pady=5)

window.mainloop()