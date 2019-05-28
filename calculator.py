import tkinter as tk

mainWindow = tk.Tk()
mainWindow.title('Calculator | Python Project')

headingLabel1 = tk.Label(mainWindow, text="Enter the first number", padx=30, pady=5)
headingLabel1.pack()

firstNumberField = tk.Entry(mainWindow)
firstNumberField.pack()

def firstNumberInput():
    firstNumber = firstNumberField.get()
    return firstNumber

headingLabel2 = tk.Label(mainWindow, text="Enter the first number", padx=30, pady=5)
headingLabel2.pack()

secondNumberField = tk.Entry(mainWindow)
secondNumberField.pack()

def secondNumberInput():
    secondNumber = secondNumberField.get()
    return secondNumber

headingLabel3 = tk.Label(mainWindow, text="Result", padx=30, pady=5)
headingLabel3.pack()

result = tk.StringVar()
resultField = tk.Entry(mainWindow, textvariable=result)
resultField.pack()

button1 = tk.Button(mainWindow, text='+', command=lambda: result.set(int(firstNumberInput())+int(secondNumberInput())))
button1.pack()

button2 = tk.Button(mainWindow, text='-', command=lambda: result.set(int(firstNumberInput())-int(secondNumberInput())))
button2.pack()

button3 = tk.Button(mainWindow, text='*', command=lambda: result.set(int(firstNumberInput())*int(secondNumberInput())))
button3.pack()

button4 = tk.Button(mainWindow, text='/', command=lambda: result.set(int(firstNumberInput())/int(secondNumberInput())))
button4.pack()

mainWindow.mainloop()