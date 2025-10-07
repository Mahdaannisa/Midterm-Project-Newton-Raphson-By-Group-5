import tkinter as tk
from tkinter import ttk, messagebox
from core.formatter import format_persamaan, fmt_excel
from core.newton import newton_raphson
from core.plotter import tampilkan_plot

class NewtonApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Metode Newton-Raphson")
        self.root.geometry("1200x700")
        self.root.configure(bg="#1b0f08")

        tk.Label(root, text="Metode Newton-Raphson",
                 font=("Segoe UI", 18, "bold"),
                 fg="#fff3e3", bg="#1b0f08").pack(pady=10)

        frame = tk.Frame(root, bg="#1b0f08")
        frame.pack(fill="both", expand=True, padx=20, pady=10)

        left = tk.Frame(frame, bg="#1b0f08")
        left.pack(side="left", fill="both", expand=True)

        form = tk.Frame(left, bg="#2f1f15", padx=10, pady=10)
        form.pack(fill="x", pady=5)

        tk.Label(form, text="Fungsi f(x):", bg="#2f1f15", fg="#fff3e3", font=("Segoe UI", 11)).grid(row=0, column=0, sticky="e", pady=4)
        self.ent_fx = tk.Entry(form, width=40, font=("Segoe UI", 11))
        self.ent_fx.insert(0, "4x^3 - 15x^2 + 17x - 6=0")
        self.ent_fx.grid(row=0, column=1, pady=4)

        tk.Label(form, text="x₀ (tebakan awal):", bg="#2f1f15", fg="#fff3e3", font=("Segoe UI", 11)).grid(row=1, column=0, sticky="e", pady=4)
        self.ent_x0 = tk.Entry(form, width=10, font=("Segoe UI", 11))
        self.ent_x0.insert(0, "3")
        self.ent_x0.grid(row=1, column=1, sticky="w", pady=4)

        tk.Label(form, text="Jumlah Iterasi (N):", bg="#2f1f15", fg="#fff3e3", font=("Segoe UI", 11)).grid(row=2, column=0, sticky="e", pady=4)
        self.ent_n = tk.Entry(form, width=10, font=("Segoe UI", 11))
        self.ent_n.insert(0, "10")
        self.ent_n.grid(row=2, column=1, sticky="w", pady=4)

        tk.Label(form, text="Galat (ε):", bg="#2f1f15", fg="#fff3e3", font=("Segoe UI", 11)).grid(row=3, column=0, sticky="e", pady=4)
        self.ent_tol = tk.Entry(form, width=10, font=("Segoe UI", 11))
        self.ent_tol.insert(0, "0.001")
        self.ent_tol.grid(row=3, column=1, sticky="w", pady=4)

        btn_frame = tk.Frame(form, bg="#2f1f15")
        btn_frame.grid(row=4, column=0, columnspan=2, pady=8)

        tk.Button(btn_frame, text="Hitung", bg="#caa77e", fg="#1b0f08",
                  font=("Segoe UI", 11, "bold"), width=10,
                  command=self.hitung).pack(side="left", padx=5)

        tk.Button(btn_frame, text="Plot (samping)", bg="#a67b5b", fg="white",
                  font=("Segoe UI", 11, "bold"), width=12,
                  command=self.plot).pack(side="left", padx=5)

        self.label_hasil = tk.Label(left, text="", bg="#1b0f08", fg="#fff3e3", font=("Segoe UI", 10, "italic"))
        self.label_hasil.pack(pady=5)

        table_frame = tk.Frame(left, bg="#1b0f08")
        table_frame.pack(fill="both", expand=True, pady=5)

        self.tree = ttk.Treeview(table_frame, columns=("i", "xi", "fxi", "dfxi"), show="headings")
        self.tree.heading("i", text="Iterasi")
        self.tree.heading("xi", text="xi")
        self.tree.heading("fxi", text="f(xi)")
        self.tree.heading("dfxi", text="f'(xi)")
        for c in ("i", "xi", "fxi", "dfxi"):
            self.tree.column(c, anchor="center", width=160)
        self.tree.pack(fill="both", expand=True, padx=5, pady=5)

        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"), background="#f5d37b", foreground="#000")
        style.configure("Treeview", font=("Segoe UI", 10), rowheight=26, background="#fff", fieldbackground="#fff")
        style.map("Treeview", background=[("selected", "#e7c9a3")])

        self.plot_frame = tk.Frame(frame, bg="#1b0f08")
        self.plot_frame.pack(side="right", fill="both", expand=True, padx=10)

