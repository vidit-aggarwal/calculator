import tkinter as tk
from tkinter import messagebox as mb
main_window = tk.Tk()
main_window.title("Basic Calculator")

try:
    label1 = tk.Label(main_window, text="Enter First Number")
    label1.grid(row=0, column=0, padx=10, pady=10, sticky="W")

    n1 = tk.StringVar()
    number_field1 = tk.Entry(main_window, textvariable=n1, width=10)
    number_field1.grid(row=0, column=1, padx=10, pady=10)

    label2 = tk.Label(main_window, text="Enter Second Number")
    label2.grid(row=1, column=0, padx=10, pady=10, sticky="W")

    n2 = tk.StringVar()
    number_field2 = tk.Entry(main_window, textvariable=n2, width=10)
    number_field2.grid(row=1, column=1, padx=10, pady=10)

    label3 = tk.Label(main_window, text="Result")
    label3.grid(row=2, column=0, padx=10, pady=10, sticky="W")

    result = tk.StringVar()
    result_field = tk.Entry(main_window, width=10, textvariable=result)
    result_field.grid(row=2, column=1, padx=10, pady=10)

    add = tk.Button(main_window, text='+', activebackground='grey', activeforeground='white', width=20, height=1,
                    command=lambda: addition())
    add.grid(row=3, column=0, padx=(10, 0), pady=(10, 0), sticky="W")

    subtract = tk.Button(main_window, text='-', activebackground='grey', activeforeground='white', width=20, height=1,
                         command=lambda:substraction())
    subtract.grid(row=3, column=1, padx=(0, 10), pady=(10, 0), sticky="W")

    divide = tk.Button(main_window, text='/', activebackground='grey', activeforeground='white', width=20, height=1,
                       command=lambda: division())
    divide.grid(row=4, column=0, padx=(10, 0), pady=(0, 10), sticky="W")

    multiply = tk.Button(main_window, text='*', activebackground='grey', activeforeground='white', width=20, height=1,
                         command=lambda: multiplication())
    multiply.grid(row=4, column=1, padx=(0, 10), pady=(0, 10), sticky="W")


    def addition():
        try:
            num1 = float(number_field1.get())
            num2 = float(number_field2.get())
            res = num1 + num2
            display(res)
        except(ValueError):
            mb.showerror("ValueError", "Please enter an Integer or Float Value.")
            n1.set("")
            n2.set("")

        except(ZeroDivisionError):
            mb.showerror("ZeroDivisionError", "Value of second number cannot be 0.")
            n2.set("")

    def substraction():
        try:
            num1 = float(number_field1.get())
            num2 = float(number_field2.get())
            res = num1 - num2
            display(res)
        except(ValueError):
            mb.showerror("ValueError", "Please enter an Integer or Float Value.")
            n1.set("")
            n2.set("")

        except(ZeroDivisionError):
            mb.showerror("ZeroDivisionError", "Value of second number cannot be 0.")
            n2.set("")

    def multiplication():
        try:
            num1 = float(number_field1.get())
            num2 = float(number_field2.get())
            res = num1 * num2
            display(res)
        except(ValueError):
            mb.showerror("ValueError", "Please enter an Integer or Float Value.")
            n1.set("")
            n2.set("")

        except(ZeroDivisionError):
            mb.showerror("ZeroDivisionError", "Value of second number cannot be 0.")
            n2.set("")


    def division():
        try:
            num1 = float(number_field1.get())
            num2 = float(number_field2.get())
            res = num1 / num2
            display(res)
        except(ValueError):
            mb.showerror("ValueError", "Please enter an Integer or Float Value.")
            n1.set("")
            n2.set("")

        except(ZeroDivisionError):
            mb.showerror("ZeroDivisionError", "Value of second number cannot be 0.")
            n2.set("")

    def display(res):
        result.set(res)

except ValueError:
    mb.showerror("ValueError", "Please enter an Integer or Float Value.")
    n1.set("")
    n2.set("")

except ZeroDivisionError:
    mb.showerror("ZeroDivisionError", "Value of second number cannot be 0.")
    n2.set("")

main_window.mainloop()
