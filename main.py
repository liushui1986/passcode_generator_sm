from tkinter import *
from tkinter import messagebox
import random
import string
import pyperclip
import json
from bokeh.layouts import column

FONT_NAME = "Courier"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation

    choice_letters = [random.choice(letters) for _ in range(random.randint(6, 10))]
    choice_symbols = [random.choice(symbols) for _ in range(random.randint(1, 4))]
    choice_numbers = [random.choice(numbers) for _ in range(random.randint(1, 4))]

    password_list = choice_letters + choice_symbols + choice_numbers
    random.shuffle(password_list)

    final_password = "".join(password_list)
    password_entry.insert(0, final_password)
    pyperclip.copy(final_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            'username': username,
            'password': password
        }
    }

    if not website or not password:
        messagebox.showinfo(title='Oops', message='Please fill any empty fields!')
    else:
        try:
            with open('data_passcode.json', 'r') as file:
                # Read old data
                data = json.load(file)
        except FileNotFoundError:
            with open('data_passcode.json', 'w') as file:
                json.dump(new_data, file, indent=4)
        else:
            # Update old data with new data
            data.update(new_data)

            with open('data_passcode.json', 'w') as file:
                # Save the updated data
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            username_entry.delete(0, END)
            username_entry.insert(0, 'mshipen1966@gmail.com')
            password_entry.delete(0, END)


# -------------------------- SEARCH PASSWORD -------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open('data_passcode.json', 'r') as file:
            # Load data
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(message='No Data File found')
    else:
        if website in data:
            username = data[website]['username']
            password = data[website]['password']
            messagebox.showinfo(title=website, message=f'Username: {username}.\n Password: {password}')
        else:
            messagebox.showerror(message='No details for the website exists!')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50, bg='white')

canvas = Canvas(width=200, height=200, bg='white')
lock_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text='Website:', bg='white', font=(FONT_NAME, 10))
website_label.grid(column=0, row=1)

user_label = Label(text='Email/Username:', bg='white', font=(FONT_NAME, 10))
user_label.grid(column=0, row=2)

password_label = Label(text='Password:', bg='white', font=(FONT_NAME, 10))
password_label.grid(column=0, row=3)

# Buttons
search_button = Button(text='Search', width=15, command=find_password)
search_button.grid(column=2, row=1)

generate_button = Button(text='Generate Password', width=15, command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text='Add', width=43, command=save)
add_button.grid(row=4, column=1, columnspan=2)

# Entries
website_entry = Entry(width=32)
website_entry.grid(column=1, row=1)
website_entry.focus()

username_entry = Entry(width=51)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(0, 'mshipen1966@gmail.com')

password_entry = Entry(width=32)
password_entry.grid(column=1, row=3)

window.mainloop()
