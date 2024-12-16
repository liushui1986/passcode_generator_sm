from tkinter import *
from tkinter import messagebox
import random
import string
import pyperclip
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

    if not website or not password:
        messagebox.showinfo(title='Oops', message='Please fill any empty fields!')
    else:
        is_ok = messagebox.askokcancel(title=website, message=f'These are the details entered: \nUsername: {username}'
                                                      f'\nPassword: {password} \nIs it OK to save?')
        if is_ok:
            with open('data_passcode.txt', 'a') as file:
                file.write(f'{website} | {username} | {password}\n')
            website_entry.delete(0, END)
            username_entry.delete(0, END)
            username_entry.insert(0, 'mshipen1966@gmail.com')
            password_entry.delete(0, END)

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
generate_button = Button(text='Generate Password', command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text='Add', width=43, command=save)
add_button.grid(row=4, column=1, columnspan=2)

# Entries
website_entry = Entry(width=50)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

username_entry = Entry(width=50)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(0, 'mshipen1966@gmail.com')

password_entry = Entry(width=32)
password_entry.grid(column=1, row=3)

window.mainloop()
