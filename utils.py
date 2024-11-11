# utils.py
import random
import string

# load in characters that will be used
chars = " " + string.punctuation + string.digits + string.ascii_letters

# turn the string into a list where each character is an individual element
chars = list(chars)
key = chars.copy()

# shuffle the key
random.shuffle(key)

# initialize the variables
plain_text = ""
cipher_text = ""

# create the file that will hold encrypted messages
file_name = "cipher_texts.txt"
with open(file_name, 'w') as file:
    file.write("Encrypted texts:\n")
    file.write("\n")

# function to submit text (encrypt.py)
def submit_encrypt(entry, result_label):
    global cipher_text
    plain_text = entry.get()
    cipher_text = "" # reset the variable each time submit button is pressed

    # iteratae over every letter in plain text
    for letter in plain_text:
        i = chars.index(letter)
        cipher_text += key[i]

    # update result label
    result_label.config(text=f"Cipher Text: {cipher_text}")

# click function (encrypt.py)
def click_encrypt(result_label, window):
    try:
        if cipher_text: # check if cipher_text has content
            if messagebox.askokcancel(title="Save cipher text?", message="Would you like to save the cipher text to a file?"):
                with open(file_name, 'a') as file:
                    file.write(cipher_text)
                    file.write("\n")
                
                if messagebox.askokcancel(title="Text saved", message="Cipher text saved to cipher_texts.txt. Return to main menu?"):
                    window.destroy()
                    os.system("python3 menu.py") # return to the main menu
                else:
                    pass
            else:
                messagebox.showwarning("Warning", "No text to save. Please generate cipher text first.")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# function to submit text (decrypt.py)
def submit_decrypt():
    global cipher_text
    plain_text = entry.get()
    cipher_text = "" # reset the variable each time submit button is pressed

    # iteratae over every letter in plain text
    for letter in plain_text:
        i = chars.index(letter)
        cipher_text += key[i]

    # update result label
    result_label.config(text=f"Cipher Text: {cipher_text}")