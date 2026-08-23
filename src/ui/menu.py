import tkinter as tk
from tkinter import filedialog, messagebox
from src.core.file_manager import FileManager

def create_menu(root: tk.Tk):
    menubar = tk.Menu(root)

    # ---- Dosya ----
    file_menu = tk.Menu(menubar, tearoff=0)
    file_menu.add_command(label="Yeni", accelerator="Ctrl+N",
                          command=lambda: root.event_generate("<<New>>"))
    file_menu.add_command(label="Aç...", accelerator="Ctrl+O",
                          command=lambda: root.event_generate("<<Open>>"))
    file_menu.add_separator()
    file_menu.add_command(label="Kaydet", accelerator="Ctrl+S",
                          command=lambda: root.event_generate("<<Save>>"))
    file_menu.add_command(label="Farklı Kaydet...", accelerator="Ctrl+Shift+S",
                          command=lambda: root.event_generate("<<SaveAs>>"))
    file_menu.add_separator()
    file_menu.add_command(label="Çıkış", accelerator="Ctrl+Q",
                          command=root.quit)
    menubar.add_cascade(label="Dosya", menu=file_menu)

    # ---- Düzen ----
    edit_menu = tk.Menu(menubar, tearoff=0)
    edit_menu.add_command(label="Geri Al", accelerator="Ctrl+Z",
                          command=lambda: root.text.edit_undo())
    edit_menu.add_command(label="İleri Al", accelerator="Ctrl+Y",
                          command=lambda: root.text.edit_redo())
    edit_menu.add_separator()
    edit_menu.add_command(label="Kes", accelerator="Ctrl+X",
                          command=lambda: root.text.event_generate("<<Cut>>"))
    edit_menu.add_command(label="Kopyala", accelerator="Ctrl+C",
                          command=lambda: root.text.event_generate("<<Copy>>"))
    edit_menu.add_command(label="Yapıştır", accelerator="Ctrl+V",
                          command=lambda: root.text.event_generate("<<Paste>>"))
    menubar.add_cascade(label="Düzen", menu=edit_menu)

    # ---- Yardım ----
    help_menu = tk.Menu(menubar, tearoff=0)
    help_menu.add_command(label="Hakkında", command=_show_about)
    menubar.add_cascade(label="Yardım", menu=help_menu)

    root.config(menu=menubar)

    # ---- Event Handlers ----
    root.bind("<<New>>", lambda e: _new_file(root))
    root.bind("<<Open>>", lambda e: _open_file(root))
    root.bind("<<Save>>", lambda e: _save_file(root))
    root.bind("<<SaveAs>>", lambda e: _save_as_file(root))

def _new_file(root):
    if _maybe_save(root):
        root.text.delete("1.0", tk.END)
        root.title("Küçük Not Defteri - Yeni")
        root.current_file = None

def _open_file(root):
    if not _maybe_save(root):
        return
    path = filedialog.askopenfilename(
        filetypes=[("Metin Dosyaları", "*.txt"), ("Tüm Dosyalar", "*.*")]
    )
    if path:
        content = FileManager.read(path)
        root.text.delete("1.0", tk.END)
        root.text.insert(tk.END, content)
        root.title(f"Küçük Not Defteri - {path}")
        root.current_file = path

def _save_file(root):
    if hasattr(root, "current_file") and root.current_file:
        FileManager.write(root.current_file, root.text.get("1.0", tk.END))
    else:
        _save_as_file(root)

def _save_as_file(root):
    path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Metin Dosyaları", "*.txt"), ("Tüm Dosyalar", "*.*")]
    )
    if path:
        FileManager.write(path, root.text.get("1.0", tk.END))
        root.current_file = path
        root.title(f"Küçük Not Defteri - {path}")

def _maybe_save(root) -> bool:
    """Kullanıcıya kaydetme sorusu sorar, evet ise kaydeder."""
    if root.text.edit_modified():
        answer = messagebox.askyesnocancel(
            "Değişiklikler kaydedilsin mi?",
            "Kaydedilmemiş değişiklikler var. Şimdi kaydetmek ister misiniz?"
        )
        if answer is None:   # Cancel
            return False
        if answer:           # Yes
            _save_file(root)
    return True

def _show_about():
    messagebox.showinfo(
        "Hakkında",
        "Küçük Not Defteri\nVersiyon 1.0\nPython + Tkinter ile geliştirilmiştir."
    )
