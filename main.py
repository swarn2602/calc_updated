import math
import tkinter as tk

# Function to evaluate the expression
def evaluate_expression():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to perform square root operation
def square_root():
    try:
        result = math.sqrt(float(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main window
window = tk.Tk()
window.title("Scientific Calculator")

# Create the entry widget
entry = tk.Entry(window, width=25)
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

# Create the number buttons
numbers = ['7', '8', '9', '4', '5', '6', '1', '2', '3', '0']
row = 1
col = 0
for number in numbers:
    button = tk.Button(window, text=number, width=5, command=lambda num=number: entry.insert(tk.END, num))
    button.grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col == 3:
        col = 0
        row += 1

# Create the operator buttons
operators = ['+', '-', '*', '/']
row = 1
col = 3
for operator in operators:
    button = tk.Button(window, text=operator, width=5, command=lambda op=operator: entry.insert(tk.END, op))
    button.grid(row=row, column=col, padx=5, pady=5)
    row += 1

# Create the special function buttons
sqrt_button = tk.Button(window, text="sqrt", width=5, command=square_root)
sqrt_button.grid(row=1, column=4, padx=5, pady=5)

equal_button = tk.Button(window, text="=", width=5, command=evaluate_expression)
equal_button.grid(row=4, column=4, padx=5, pady=5)

clear_button = tk.Button(window, text="C", width=5, command=lambda: entry.delete(0, tk.END))
clear_button.grid(row=4, column=0, padx=5, pady=5)

# Run the main loop
window.mainloop()
