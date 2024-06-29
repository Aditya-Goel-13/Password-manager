from tkinter import *
from tkinter import messagebox
from random import shuffle, choice, randint
import pyperclip
import json


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_pass():
    web = web_input.get().title()
    if len(web) == 0:
        messagebox.showinfo(title="Error", message="Required field is empty")
        return
    try:
        with open("Passwords.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found")
    else:
        if web in data:
            req_password = data[web]["password"]
            req_email = data[web]["email"]
            messagebox.showinfo(title=web, message=f"email: {req_email}\npassword: {req_password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for the{web} found")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_char = [choice(letters) for _ in range(randint(6, 8))]
    password_symb = [choice(symbols) for _ in range(randint(2, 4))]
    password_num = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_num + password_symb + password_char
    shuffle(password_list)

    rand_password = "".join(password_list)

    pass_input.delete(0, END)
    pass_input.insert(END, rand_password)
    pyperclip.copy(rand_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web = web_input.get().title()
    emails = email_input.get()
    passwords = pass_input.get()
    new_data = {
        web: {
            "email": emails,
            "password": passwords
        }
    }
    if web == "" or emails == "" or passwords == "":
        messagebox.showinfo(title="Website", message="Empty fields are not allowed")
    else:
        try:
            with open("Passwords.json", "r") as file:
                data = json.load(file)
                data.update(new_data)
        except:
            with open("Passwords.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            with open("Passwords.json", mode="w") as file:
                json.dump(data, file, indent=4)
        finally:
            web_input.delete(0, END)
            pass_input.delete(0, END)
            web_input.focus()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

# canvas
canvas = Canvas(height=200, width=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# Labels
website = Label(text="Website:")
website.grid(row=1, column=0)
email = Label(text="Email/Username:")
email.grid(row=2, column=0)
password = Label(text="Password:")
password.grid(row=3, column=0)

# Entries
pass_input = Entry(width=32)
pass_input.grid(row=3, column=1, sticky="w")
web_input = Entry(width=32)
web_input.focus()
web_input.grid(row=1, column=1, sticky="w")
email_input = Entry(width=35)
email_input.insert(END, "adigoel@gmail.com")
email_input.grid(row=2, column=1, columnspan=2, sticky="ew")

add_button = Button(text="Add",width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="ew")
generate = Button(text="Generate Password", width=15, command=generate)
generate.grid(row=3, column=2, sticky="ew")
search = Button(text="Search", command=search_pass)
search.grid(row=1, column=2, sticky="ew")

window.mainloop()
