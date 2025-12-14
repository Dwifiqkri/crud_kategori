import tkinter as tk
from tkinter import ttk
from presenter.kategori_presenter import KategoriPresenter

class KategoriView(tk.Tk):
    def __init__(self):
        print(">>> VIEW INIT START")   # 👈 DI SINI

        super().__init__()

        self.title("CRUD Kategori Buku")
        self.geometry("400x350")

        # Input
        self.entry_nama = tk.Entry(self)
        self.entry_nama.pack(pady=5)

        self.btn_tambah = tk.Button(self, text="Tambah", command=self.tambah)
        self.btn_tambah.pack()

        # Table
        self.tree = ttk.Treeview(self, columns=("id", "nama"), show="headings")
        self.tree.heading("id", text="ID")
        self.tree.heading("nama", text="Nama Kategori")
        self.tree.pack(expand=True, fill="both", pady=10)

        self.btn_hapus = tk.Button(self, text="Hapus", command=self.hapus)
        self.btn_hapus.pack()

        # Presenter
        self.presenter = KategoriPresenter(self)

        print(">>> VIEW INIT END")     # 👈 BOLEH TAMBAH INI
