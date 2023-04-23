import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from tkinter import messagebox

window = tk.Tk()
window.title('Simple Calculator')
window.geometry('500x180')

def addFormula():
    value1 = num1.get()
    value1_int = int(value1)
    value2 = num2.get()
    value2_int = int(value2)
    result = value1_int+value2_int
    reLbl.config(text=str(result))


def subForm():
    value1 = num1.get()
    value1_int = int(value1)
    value2 = num2.get()
    value2_int = int(value2)
    result = value1_int-value2_int
    reLbl.config(text=str(result))


def mulForm():
    value1 = num1.get()
    value1_int = int(value1)
    value2 = num2.get()
    value2_int = int(value2)
    result = value1_int*value2_int
    reLbl.config(text=str(result))


def divForm():
    value1 = num1.get()
    value1_int = int(value1)
    value2 = num2.get()
    value2_int = int(value2)
    result = value1_int/value2_int
    reLbl.config(text=str(result))

    
    

lbl1 = tk.Label(window, text = "Enter first number:")
lbl1.grid(row = 0, column = 0)
num1 = tk.Entry(window)
num1.grid(row=0, column=1, padx=20)

lbl2 = tk.Label(window, text="Enter second number:")
lbl2.grid(row=1, column=0)
num2 = tk.Entry(window)
num2.grid(row=1, column=1, pady=10)

reLbl = tk.Label(window, text='', font=('Roboto',20))
reLbl.grid(row=1, column=3, padx=20)

addButton = tk.Button(window, text="Add", activebackground='black', activeforeground='white', command = addFormula)
addButton.grid(row=2, column=0)
sButton = tk.Button(window, text="Subtract", activebackground='black', activeforeground='white', command = subForm)
sButton.grid(row=2, column=1)
mButton = tk.Button(window, text="Multiply", activebackground='black', activeforeground='white', command = mulForm)
mButton.grid(row=2, column=2)
dButton = tk.Button(window, text="Divide", activebackground='black', activeforeground='white', command = divForm)
dButton.grid(row=3, column=0, pady=13)



window.mainloop()
