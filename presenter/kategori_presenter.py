from model.kategori_model import KategoriModel

class KategoriPresenter:
    def __init__(self, view):
        print("PRESENTER INIT")
        self.view = view
        self.model = KategoriModel()

    def load_data(self):
        print("LOAD DATA")
        data = self.model.get_all()
        self.view.tampilkan_data(data)

    def tambah_kategori(self, nama):
        if nama.strip() == "":
            return
        self.model.insert(nama)
        self.load_data()

    def hapus_kategori(self, kategori_id):
        self.model.delete(kategori_id)
        self.load_data()
