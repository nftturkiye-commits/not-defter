import tkinter as tk
from src.ui.menu import create_menu
from src.ui.toolbar import create_toolbar
from src.ui.statusbar import create_statusbar

class NotDefteri(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Küçük Not Defteri")
        self.geometry("800x600")
        self._create_widgets()

    def _create_widgets(self):
        # Menü
        create_menu(self)

        # Araç çubuğu
        self.toolbar = create_toolbar(self)

        # Metin alanı
        self.text = tk.Text(self, wrap="word", undo=True)
        self.text.pack(fill="both", expand=True, side="top")

        # Durum çubuğu
        self.status = create_statusbar(self)

        # Kısayol bağlamaları
        self._bind_shortcuts()

    def _bind_shortcuts(self):
        self.bind("<Control-n>", lambda e: self.event_generate("<<New>>"))
        self.bind("<Control-o>", lambda e: self.event_generate("<<Open>>"))
        self.bind("<Control-s>", lambda e: self.event_generate("<<Save>>"))
        self.bind("<Control-Shift-S>", lambda e: self.event_generate("<<SaveAs>>"))
        self.bind("<Control-q>", lambda e: self.quit())

if __name__ == "__main__":
    app = NotDefteri()
    app.mainloop()
