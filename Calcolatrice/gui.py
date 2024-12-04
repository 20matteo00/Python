# gui.py
import tkinter as tk
from calc_logic import evaluate_expression
from config import *

import math

def press(key, entry):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(key))

def calculate(entry):
    try:
        result = evaluate_expression(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def clear(entry):
    entry.delete(0, tk.END)

def backspace(entry):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current[:-1])

def factorial(entry):
    try:
        num = int(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, math.factorial(num))
    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def reciprocal(entry):
    try:
        num = float(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, 1 / num)
    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def square(entry):
    try:
        num = float(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, num ** 2)
    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def square_root(entry):
    try:
        num = float(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, math.sqrt(num))
    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def toggle_sign(entry):
    try:
        num = float(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, -num)
    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def percentage(entry):
    try:
        num = float(entry.get()) / 100  # Converte il numero in percentuale
        entry.delete(0, tk.END)
        entry.insert(tk.END, num)
    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def create_calculator_window():

    # Finestra principale
    root = tk.Tk()
    root.title("Calcolatrice")
    root.geometry(f"{window_width}x{window_height}")  # Imposta la dimensione della finestra

    # Display
    entry = tk.Entry(root, width=button_width * button_for_row, font=("Arial", font_size), borderwidth=borderwidth, relief="solid", justify="right")
    entry.grid(row=0, column=0, columnspan=button_for_row, padx=padxdisplay, pady=padydisplay)

    # Definizione dei pulsanti
    buttons = [
        ('%', 1, 0), ('C', 1, 1), ('<-', 1, 2), ('!', 1, 3),
        ('1/X', 2, 0), ('X^2', 2, 1), ('Rad(X)', 2, 2), ('/', 2, 3),
        ('7', 3, 0), ('8', 3, 1), ('9', 3, 2), ('*', 3, 3),
        ('4', 4, 0), ('5', 4, 1), ('6', 4, 2), ('-', 4, 3),
        ('1', 5, 0), ('2', 5, 1), ('3', 5, 2), ('+', 5, 3),
        ('+/-', 6, 0), ('0', 6, 1), (',', 6, 2), ('=', 6, 3),
        ('(', 7, 0), (')', 7, 1),  # Aggiungi parentesi
    ]

    # Aggiungi i pulsanti alla finestra
    for (text, row, col) in buttons:
        if text == 'C':
            tk.Button(root, text=text, width=button_width, height=button_height, font=("Arial", font_size), command=lambda: clear(entry)).grid(row=row, column=col, padx=padbutton, pady=padbutton)
        elif text == '<-':
            tk.Button(root, text=text, width=button_width, height=button_height, font=("Arial", font_size), command=lambda: backspace(entry)).grid(row=row, column=col, padx=padbutton, pady=padbutton)
        elif text == '!':
            tk.Button(root, text=text, width=button_width, height=button_height, font=("Arial", font_size), command=lambda: factorial(entry)).grid(row=row, column=col, padx=padbutton, pady=padbutton)
        elif text == '1/X':
            tk.Button(root, text=text, width=button_width, height=button_height, font=("Arial", font_size), command=lambda: reciprocal(entry)).grid(row=row, column=col, padx=padbutton, pady=padbutton)
        elif text == 'X^2':
            tk.Button(root, text=text, width=button_width, height=button_height, font=("Arial", font_size), command=lambda: square(entry)).grid(row=row, column=col, padx=padbutton, pady=padbutton)
        elif text == 'Rad(X)':
            tk.Button(root, text=text, width=button_width, height=button_height, font=("Arial", font_size), command=lambda: square_root(entry)).grid(row=row, column=col, padx=padbutton, pady=padbutton)
        elif text == '+/-':
            tk.Button(root, text=text, width=button_width, height=button_height, font=("Arial", font_size), command=lambda: toggle_sign(entry)).grid(row=row, column=col, padx=padbutton, pady=padbutton)
        elif text == '%':
            tk.Button(root, text=text, width=button_width, height=button_height, font=("Arial", font_size), command=lambda: percentage(entry)).grid(row=row, column=col, padx=padbutton, pady=padbutton)
        elif text == '=':
            tk.Button(root, text=text, width=button_width, height=button_height, font=("Arial", font_size), command=lambda: calculate(entry)).grid(row=row, column=col, padx=padbutton, pady=padbutton)
        else:
            tk.Button(root, text=text, width=button_width, height=button_height, font=("Arial", font_size), command=lambda key=text: press(key, entry)).grid(row=row, column=col, padx=padbutton, pady=padbutton)

    return root
