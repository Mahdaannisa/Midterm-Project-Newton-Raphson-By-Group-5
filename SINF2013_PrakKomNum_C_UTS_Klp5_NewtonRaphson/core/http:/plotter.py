import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, sympify, lambdify
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import messagebox

def tampilkan_plot(expr_raw, master):
    from .formatter import format_persamaan
    for w in master.winfo_children():
        w.destroy()

    expr = format_persamaan(expr_raw)
    try:
        x = symbols('x')
        f = lambdify(x, sympify(expr), 'numpy')
    except Exception:
        messagebox.showerror("Error", "Persamaan tidak valid!")
        return

    xs = np.linspace(-1, 5, 400)
    ys = f(xs)
