# ---------------------------- Imports ------------------------------- #
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Function
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- PASSWORD Managment ------------------------------- #
# Save Password Function
def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    # Save website, email, and password to new_data
    new_data = {
        website: {
            "email": email,
            "password": password,
        }   
    }
    # Check if input is empty
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")    
    else:
            try: 
                with open("data.json", "r") as data_file:
                # read the data from the file using json.load
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    # write the data to the file using json.dump
                    json.dump(new_data, data_file, indent=4)
                    messagebox.showinfo(title="Success", message="Your password has been saved.")
            else:
                # update the data in the file with the new data using json.update
                data.update(new_data)     
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
                    messagebox.showinfo(title="Success", message="Your password has been saved.")
            finally:    
                website_entry.delete(0, END)
                password_entry.delete(0, END)


def find_password():
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="No passwords have been saved yet.")
    else:
        website = website_entry.get()
        if website in data:
            messagebox.showinfo(title="Success", message="Your password is: " + data[website]["password"])
        else:
            messagebox.showinfo(title="Oops", message="No password has been saved for this website.")
    

# ---------------------------- UI SETUP ------------------------------- #

# Create the window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Create the Canvas widget and set its height and width 
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
# Add the canvas to the window 
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "mTarifi4@gmail.com")

password_entry = Entry(width=35)
password_entry.grid(row=3, column=1, columnspan=2)

# Buttons
generate_password_button = Button(text="Generate Password", width=25, command=generate_password)
generate_password_button.grid(row=3, column=3)

add_button = Button(text="Add", width=55, command=save)
add_button.grid(row=4, column=1, columnspan=3)

search_button = Button(text = "Search", width= 25, command=find_password)
search_button.grid(row=1, column=3)
# ---------------------------- MAIN LOOP ------------------------------- #
window.mainloop()