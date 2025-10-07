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

    fig, ax = plt.subplots(figsize=(6, 4), dpi=100)
    fig.patch.set_facecolor("#1b0f08")
    ax.set_facecolor("#22150c")

    ax.plot(xs, ys, color="#caa77e", linewidth=2)
    ax.axhline(0, color="#fff3e3", linestyle="--")
    ax.axvline(0, color="#fff3e3", linestyle="--")

    ax.set_title("Grafik f(x)", color="#fff3e3", fontname="Segoe UI")
    ax.tick_params(colors="#fff3e3")
    for spine in ax.spines.values():
        spine.set_color("#a67d56")

    canvas = FigureCanvasTkAgg(fig, master=master)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True, padx=6, pady=6)
