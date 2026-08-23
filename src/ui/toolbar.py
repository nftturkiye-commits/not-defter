import tkinter as tk
from tkinter import ttk

def create_toolbar(root: tk.Tk):
    toolbar = ttk.Frame(root, padding=2)
    toolbar.pack(side="top", fill="x")

    # Yeni
    new_btn = ttk.Button(toolbar, text="Yeni", command=lambda: root.event_generate("<<New>>"))
    new_btn.pack(side="left", padx=2)

    # Aç
    open_btn = ttk.Button(toolbar, text="Aç", command=lambda: root.event_generate("<<Open>>"))
    open_btn.pack(side="left", padx=2)

    # Kaydet
    save_btn = ttk.Button(toolbar, text="Kaydet", command=lambda: root.event_generate("<<Save>>"))
    save_btn.pack(side="left", padx=2)

    return toolbar
