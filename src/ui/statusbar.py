import tkinter as tk

def create_statusbar(root: tk.Tk):
    status = tk.Label(root, text="Satır 1, Sütun 1", anchor="w")
    status.pack(side="bottom", fill="x")
    # Güncelleme fonksiyonu
    def update_status(event=None):
        try:
            line, column = root.text.index(tk.INSERT).split('.')
            status.config(text=f"Satır {int(line)}, Sütun {int(column)+1}")
        except Exception:
            pass
    root.text.bind("<KeyRelease>", update_status)
    root.text.bind("<ButtonRelease>", update_status)
    return status
