from tkinter import *
import tkinter.messagebox
from auto_password_generator import password
import pyperclip
import json

# -----------------------------Buttons functions----------------------------- #


def button3_click():
    with open("password_log.json") as file:
        data = json.load(file)
        if entry1.get().lower() in data:
            dictionary = data[entry1.get().lower()]
            tkinter.messagebox.showinfo(entry1.get().lower(), "Email: " + dictionary["Email"] +
                                                              "\n\nPassword: " + dictionary["Password"])
        else:
            tkinter.messagebox.showinfo("Oops!", f"Sorry, '{entry1.get()}' has no details ⚠")


def button2_click():
    code = password()
    if entry3.get() == "":
        entry3.insert(END, string=code)
        pyperclip.copy(code)
    else:
        entry3.delete(0, END)
        button2_click()


def button1_click():
    data = {
        entry1.get().lower(): {
            "Email": entry2.get(),
            "Password": entry3.get()
        }
    }
    if entry1.get() == "" or entry2.get() == "" or entry3.get() == "":
        tkinter.messagebox.showinfo("Oops!", "No fields can't empty!!")
        return
    result = tkinter.messagebox.askokcancel(f"{entry1.get()}", f"Your detail:\nEmail: {entry2.get()}"
                                                               f"\nPassword: {entry3.get()}\n"
                                                               f"is this ok?")
    if result:
        try:
            with open("password_log.json", mode="r") as file:
                j_data = json.load(file)
        except FileNotFoundError:
            with open("password_log.json", mode="w") as file:
                json.dump(data, file, indent=4)
        else:
            j_data.update(data)
            with open("password_log.json", mode="w") as file:
                json.dump(j_data, file, indent=4)
        finally:
            entry3.delete(0, END)
            entry1.delete(0, END)


# -----------------------------Manager UI----------------------------- #
window = Tk()
window.title("Password Manager")
window.minsize(425, 300)
window.config(padx=50, pady=50)

label1 = Label(text="Website:")
label2 = Label(text="Email/username:   ")
label3 = Label(text="Password:")
label1.grid(row=1, column=0)
label2.grid(row=2, column=0)
label3.grid(row=3, column=0)

canvas = Canvas(width=200, height=190)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 82, image=img)
canvas.grid(row=0, column=1)

entry1 = Entry(width=30)
entry2 = Entry(width=52)
entry2.insert(END, string="markvalloway9@gmail.com")
entry3 = Entry(width=30)
entry1.grid(row=1, column=1, sticky="w")
entry2.grid(row=2, column=1, columnspan=2, sticky="w")
entry3.grid(row=3, column=1, sticky="w")


button1 = Button(text="Add", width=44, command=button1_click)
button2 = Button(text="Generate Password", width=15, command=button2_click)
button3 = Button(text="Search", width=15, command=button3_click)
button1.grid(row=4, column=1, columnspan=2, sticky="w")
button2.grid(row=3, column=2, sticky="w")
button3.grid(row=1, column=2, sticky="w")

window.mainloop()
