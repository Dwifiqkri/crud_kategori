import tkinter as tk
from tkinter import ttk
from presenter.kategori_presenter import KategoriPresenter

class KategoriView(tk.Tk):
    def __init__(self):
        print(">>> VIEW INIT START")

        super().__init__()

        self.title("CRUD Kategori Buku")
        self.geometry("400x350")

        # ===== INPUT =====
        tk.Label(self, text="Nama Kategori").pack(pady=5)

        self.entry_nama = tk.Entry(self)
        self.entry_nama.pack(pady=5)

        self.btn_tambah = tk.Button(
            self,
            text="Tambah",
            command=self.tambah
        )
        self.btn_tambah.pack(pady=5)

        # ===== TABLE =====
        self.tree = ttk.Treeview(
            self,
            columns=("id", "nama"),
            show="headings"
        )
        self.tree.heading("id", text="ID")
        self.tree.heading("nama", text="Nama Kategori")
        self.tree.pack(expand=True, fill="both", pady=10)

        # ===== BUTTON HAPUS =====
        self.btn_hapus = tk.Button(
            self,
            text="Hapus",
            command=self.hapus
        )
        self.btn_hapus.pack(pady=5)

        # ===== PRESENTER =====
        self.presenter = KategoriPresenter(self)

        print(">>> VIEW INIT END")

    def tampilkan_data(self, data):
        self.tree.delete(*self.tree.get_children())
        for row in data:
            self.tree.insert("", "end", values=row)

    def tambah(self):
        nama = self.entry_nama.get()
        self.presenter.tambah_kategori(nama)
        self.entry_nama.delete(0, tk.END)

    def hapus(self):
        selected = self.tree.selection()
        if not selected:
            return
        item = self.tree.item(selected[0])
        kategori_id = item["values"][0]
        self.presenter.hapus_kategori(kategori_id)
