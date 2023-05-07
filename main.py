
from tkinter import * # import the tkinter library

# define the main window
window = Tk()
window.title("Calculator") # set the title

# define the textbox
textbox = Entry(window, width=35, borderwidth=5)
textbox.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# define the functions
def button_click(number):
    # insert the number into the textbox
    current = textbox.get()
    textbox.delete(0, END)
    textbox.insert(0, str(current) + str(number))

def button_clear():
    # clear the contents of the textbox
    textbox.delete(0, END)

def button_add():
    # add two numbers
    first_number = textbox.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    textbox.delete(0, END)

def button_equal():
    # calculate the result
    second_number = textbox.get()
    textbox.delete(0, END)

    if math == "addition":
        textbox.insert(0, f_num + int(second_number))

    if math == "subtraction":
        textbox.insert(0, f_num - int(second_number))

    if math == "multiplication":
        textbox.insert(0, f_num * int(second_number))

    if math == "division":
        textbox.insert(0, f_num / int(second_number))

def button_subtract():
    # subtract two numbers
    first_number = textbox.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    textbox.delete(0, END)

def button_multiply():
    # multiply two numbers
    first_number = textbox.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    textbox.delete(0, END)

def button_divide():
    # divide two numbers
    first_number = textbox.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    textbox.delete(0, END)

# define the buttons
button_1 = Button(window, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(window, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(window, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(window, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(window, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(window, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(window, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(window, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(window, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(window, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_add = Button(window, text="+", padx=39, pady=20, command=button_add)
button_equal = Button(window, text="=", padx=91, pady=20, command=button_equal)
button_clear = Button(window, text="Clear", padx=79, pady=20, command=button_clear)
button_subtract = Button(window, text="-", padx=41, pady=20, command=button_subtract)
button_multiply = Button(window, text="*", padx=40, pady=20, command=button_multiply)
button_divide = Button(window, text="/", padx=41, pady=20, command=button_divide)

# display the buttons
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

window.mainloop()
