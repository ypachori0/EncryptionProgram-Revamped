# home.py
from tkinter import *
import os

# run utils.py when app starts
os.system("python3 utils.py")

# function to open the main menu
def open_menu():
    window.destroy() # close the home window
    os.system("python3 menu.py") # opens menu.py


# create window
window = Tk()

# set window size
window.geometry("854x480")

# set window title
window.title("Encryption Program: Home Page")

# add a label
label = Label(window,
text="Welcome to the Encrypter!",
font=('Helvetica', 24, 'bold'),
padx=10,
pady=10)
label.pack()

# add button
button = Button(window,
text="Enter",
command=open_menu)
button.pack(pady=20)

# run the app
window.mainloop()