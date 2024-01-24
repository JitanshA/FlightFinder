from tkinter import *
from tkinter import messagebox
import requests
import os
from dotenv import load_dotenv

load_dotenv()

SHEETY_USERS_ENDPOINT = os.getenv('SHEETY_USERS_ENDPOINT')


def save_details():
    email_to_save = email_input.get()
    first_name_to_save = first_name_input.get()
    last_name_to_save = last_name_input.get()

    if first_name_to_save == "" or last_name_to_save == "" or email_to_save == "":
        messagebox.showinfo(message="Please don't leave any fields empty!")
    else:
        body = {
            "user": {
                "firstName": first_name_to_save,
                "lastName": last_name_to_save,
                "email": email_to_save,
            }
        }

        response = requests.post(url=SHEETY_USERS_ENDPOINT, json=body)
        response.raise_for_status()
        print(response.text)


window = Tk()

window.title("Flight Club")
window.geometry("400x200")
window.config(padx=40, pady=40)

# Create other widgets
email_label = Label(window, text="Email:")
email_label.grid(row=1, column=0)

first_name_label = Label(window, text="First Name:")
first_name_label.grid(row=2, column=0)

last_name_label = Label(window, text="Last Name:")
last_name_label.grid(row=3, column=0)

email_input = Entry(window, width=21)
email_input.grid(row=1, column=1, columnspan=2)
email_input.focus()

first_name_input = Entry(window, width=21)
first_name_input.grid(row=2, column=1, columnspan=2)

last_name_input = Entry(window, width=21)
last_name_input.grid(row=3, column=1, columnspan=2)

add_button = Button(window, text="Add", width=18, command=save_details)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
