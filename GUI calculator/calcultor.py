from tkinter import *

# ------------------------------------- functionality ------------------------------------- #


def zero():
    main_entry.insert(END, string="0")


def one():
    main_entry.insert(END, string="1")


def two():
    main_entry.insert(END, string="2")


def three():
    main_entry.insert(END, string="3")


def four():
    main_entry.insert(END, string="4")


def five():
    main_entry.insert(END, string="5")


def six():
    main_entry.insert(END, string="6")


def seven():
    main_entry.insert(END, string="7")


def eight():
    main_entry.insert(END, string="8")


def nine():
    main_entry.insert(END, string="9")


def all_clear():
    main_entry.delete(0, END)


def clear_back():
    main_entry.delete(len(main_entry.get())-1, END)


def point():
    if "." not in main_entry.get():
        main_entry.insert(END, string=".")


def sign_changer():
    if main_entry.get() != "":
        a = main_entry.get()
        if "-" == a[0]:
            main_entry.delete(0)
            return
        if "-" != a[0]:
            main_entry.insert(0, string="-")


def add():
    if main_entry.get() != "":
        a = main_entry.get()
        if a[len(main_entry.get())-1] != "+":
            if a[len(main_entry.get())-1] == "-" or a[len(main_entry.get())-1] == "*" \
                    or a[len(main_entry.get()) - 1] == "/":
                main_entry.delete(len(main_entry.get()) - 1, END)
            if a[len(main_entry.get()) - 1] != "+":
                main_entry.insert(END, string="+")


def sub():
    if main_entry.get() != "":
        a = main_entry.get()
        if a[len(main_entry.get())-1] != "-":
            if a[len(main_entry.get())-1] == "+" or a[len(main_entry.get())-1] == "*" \
                    or a[len(main_entry.get()) - 1] == "/":
                main_entry.delete(len(main_entry.get()) - 1, END)
            if a[len(main_entry.get()) - 1] != "-":
                main_entry.insert(END, string="-")


def mul():
    if main_entry.get() != "":
        a = main_entry.get()
        if a[len(main_entry.get())-1] != "*":
            if a[len(main_entry.get())-1] == "-" or a[len(main_entry.get())-1] == "+" \
                    or a[len(main_entry.get()) - 1] == "/":
                main_entry.delete(len(main_entry.get()) - 1, END)
            if a[len(main_entry.get()) - 1] != "*":
                main_entry.insert(END, string="*")


def div():
    if main_entry.get() != "":
        a = main_entry.get()
        if a[len(main_entry.get())-1] != "/":
            if a[len(main_entry.get())-1] == "-" or a[len(main_entry.get())-1] == "*" \
                    or a[len(main_entry.get()) - 1] == "+":
                main_entry.delete(len(main_entry.get()) - 1, END)
            if a[len(main_entry.get()) - 1] != "/":
                main_entry.insert(END, string="/")


def equal():
    a = main_entry.get()
    if a[len(main_entry.get())-1] == "+" or a[len(main_entry.get())-1] == "-" or a[len(main_entry.get())-1] == "*" \
            or a[len(main_entry.get()) - 1] == "/":
        main_entry.delete(len(main_entry.get()) - 1, END)
        equal()
    try:
        result = eval(a)
    except SyntaxError:
        pass
    else:
        if main_entry.get() != "":
            main_entry.delete(0, END)
        main_entry.insert(END, string=str(result))


# ------------------------------------- UI ------------------------------------- #
window = Tk()
window.title("Calculator")

main_entry = Entry(width=11)
main_entry.insert(END, string="")
main_entry.focus()
main_entry.config(font=("Arial", 30, "normal"))
main_entry.grid(row=0, column=0, columnspan=4,  ipadx=6)

button0 = Button(text="0", font=("Terminal", 15, "bold"), command=zero)
button0.config(width=5, height=2)
button1 = Button(text="1", font=("Terminal", 15, "bold"), command=one)
button1.config(width=5, height=2)
button2 = Button(text="2", font=("Terminal", 15, "bold"), command=two)
button2.config(width=5, height=2)
button3 = Button(text="3", font=("Terminal", 15, "bold"), command=three)
button3.config(width=5, height=2)
button4 = Button(text="4", font=("Terminal", 15, "bold"), command=four)
button4.config(width=5, height=2)
button5 = Button(text="5", font=("Terminal", 15, "bold"), command=five)
button5.config(width=5, height=2)
button6 = Button(text="6", font=("Terminal", 15, "bold"), command=six)
button6.config(width=5, height=2)
button7 = Button(text="7", font=("Terminal", 15, "bold"), command=seven)
button7.config(width=5, height=2)
button8 = Button(text="8", font=("Terminal", 15, "bold"), command=eight)
button8.config(width=5, height=2)
button9 = Button(text="9", font=("Terminal", 15, "bold"), command=nine)
button9.config(width=5, height=2)
add_button = Button(text="➕", font=("Terminal", 15, "bold"), command=add)
add_button.config(width=5, height=2)
sub_button = Button(text="➖", font=("Terminal", 15, "bold"), command=sub)
sub_button.config(width=5, height=2)
mul_button = Button(text="✖", font=("Terminal", 15, "bold"), command=mul)
mul_button.config(width=5, height=2)
dvi_button = Button(text="➗", font=("Terminal", 15, "bold"), command=div)
dvi_button.config(width=5, height=2)
equal_button = Button(text="=", font=("Terminal", 15, "bold"), command=equal)
equal_button.config(width=5, height=2)
sign_button = Button(text="➕➖", font=("Terminal", 15, "bold"), command=sign_changer)
sign_button.config(width=5, height=2)
point_button = Button(text=".", font=("Terminal", 15, "bold"), command=point)
point_button.config(width=5, height=2)
all_clear_button = Button(text="C", font=("Terminal", 15, "bold"), command=all_clear)
all_clear_button.config(width=11, height=2, bg="gray")
clear_back_button = Button(text="⬅", font=("Terminal", 15, "bold"), command=clear_back)
clear_back_button.config(width=5, height=2)

all_clear_button.grid(row=1, column=0, columnspan=2, sticky="w")
clear_back_button.grid(row=1, column=2, sticky="w")
dvi_button.grid(row=1, column=3, sticky="w")
button7.grid(row=2, column=0, sticky="w")
button8.grid(row=2, column=1, sticky="w")
button9.grid(row=2, column=2, sticky="w")
mul_button.grid(row=2, column=3, sticky="w")
button4.grid(row=3, column=0, sticky="w")
button5.grid(row=3, column=1, sticky="w")
button6.grid(row=3, column=2, sticky="w")
sub_button.grid(row=3, column=3, sticky="w")
button1.grid(row=4, column=0, sticky="w")
button2.grid(row=4, column=1, sticky="w")
button3.grid(row=4, column=2, sticky="w")
add_button.grid(row=4, column=3, sticky="w")
sign_button.grid(row=5, column=0, sticky="w")
button0.grid(row=5, column=1, sticky="w")
point_button.grid(row=5, column=2, sticky="w")
equal_button.grid(row=5, column=3, sticky="w")


window.mainloop()
