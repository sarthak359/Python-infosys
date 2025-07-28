import tkinter as tk
from tkinter import messagebox

# Global Variables
expression = ""

def on_button_click(char):
    global expression
    if char == 'C':
        expression = ""
    elif char == 'DEL':
        expression = expression[:-1]
    elif char == '=':
        evaluate_expression()
        return
    else:
        expression += char
    input_text.set(expression)

def key_press(event):
    global expression
    key = event.char
    if key in '0123456789+-*/.%':
        expression += key
    elif event.keysym == "Return":
        evaluate_expression()
        return
    elif event.keysym == "BackSpace":
        expression = expression[:-1]
    elif event.keysym == "Escape":
        expression = ""
    input_text.set(expression)

def evaluate_expression():
    global expression
    try:
        if '..' in expression:
            raise ValueError("Invalid input")
        result = str(eval(expression))
        input_text.set(result)
        expression = result
    except ZeroDivisionError:
        input_text.set("Error: DivBy0")
        expression = ""
    except Exception:
        input_text.set("Error")
        expression = ""

# GUI Setup
root = tk.Tk()
root.title("Calculator")
root.geometry("380x420")
root.resizable(False, False)

input_text = tk.StringVar()

# Display
input_frame = tk.Frame(root, height=50, bd=0)
input_frame.pack(side="top", fill="both")

input_field = tk.Entry(
    input_frame,
    font=('Arial', 24),
    textvariable=input_text,
    justify='right',
    bd=10,
    relief='sunken'
)
input_field.pack(fill="both", ipady=10)

# Buttons
buttons_frame = tk.Frame(root)
buttons_frame.pack()

buttons = [
    ['C', 'DEL', '%', '/'],
    ['7', '8', '9', '*'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '+'],
    ['0', '.', '=', '']
]

for row_index, row in enumerate(buttons):
    for col_index, button_text in enumerate(row):
        if button_text:
            button = tk.Button(
                buttons_frame,
                text=button_text,
                font=('Arial', 18),
                height=2,
                width=5,
                command=lambda txt=button_text: on_button_click(txt)
            )
            button.grid(row=row_index, column=col_index, padx=5, pady=5)

# Keyboard Support
root.bind("<Key>", key_press)
root.mainloop()
