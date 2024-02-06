from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# Description:
# An efficient password generator and management tool built with Python,
# utilizing the tkinter library for GUI creation.
# This application utilizes lists and dictionaries for password generation
# and saving data. Simply click 'Generate' to create a new password, and 'Save'
# to store it in a JSON file. The app intelligently manages data, creating a new
# JSON file or updating an existing one based on your entries.
# Use the 'Search' function to find stored passwords by name,
# displaying associated email and password details instantly.


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letter = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letter + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    pass_input.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    # Using get method to get the data from the inputs
    website = web_input.get()
    email = email_input.get()
    password = pass_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please dont leave any fields empty")
    else:
        try:
            with open("data.json", mode="r") as data_file:
                # Reading the old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                # Saving the updated data
                json.dump(new_data, data_file, indent=4)

        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", mode="w") as data_file:
                # Saving the updated data
                json.dump(data, data_file, indent=4)
        finally:
            web_input.delete(0, END)
            pass_input.delete(0, END)


def search_password():
    website = web_input.get()
    try:
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website,  message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas = Canvas(width=200, height=200,  highlightthickness=0)
img_lock = PhotoImage(file="logo.png")
canvas.create_image(120, 120, image=img_lock)
canvas.grid(column=1, row=0)

# Labels
webs_label = Label(text="Website: ")
webs_label.grid(column=0, row=1)

email_label = Label(text="Email/Username: ")
email_label.grid(column=0, row=2)

pass_label = Label(text="Password: ")
pass_label.grid(column=0, row=3)


# Entries
web_input = Entry(width=35)
web_input.grid(column=1, row=1, columnspan=2)
# Focus method is for when the program start the cursor is already in website entry
web_input.focus()

email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "teoemei3@outlook.com.gr")

pass_input = Entry(width=35)
pass_input.grid(column=1, row=3, columnspan=2)


# Buttons
search_button = Button(text="Search", width=15, command=search_password)
search_button.grid(column=3, row=1)

gener_button = Button(text="Generate Password", width=15, command=generate_password)
gener_button.grid(column=3, row=3)

add_button = Button(text="Add", width=46, command=save_data)
add_button.grid(column=1, row=4, columnspan=3)


window.mainloop()
