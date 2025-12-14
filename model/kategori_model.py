from config import get_connection

class KategoriModel:
    def get_all(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT kategori_id, nama_kategori FROM kategori"
            )
            data = cursor.fetchall()
            conn.close()
            return data
        except Exception as e:
            print("ERROR GET:", e)
            return []

    def insert(self, nama):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO kategori (nama_kategori) VALUES (%s)",
                (nama,)
            )
            conn.commit()
            conn.close()
        except Exception as e:
            print("ERROR INSERT:", e)

    def delete(self, kategori_id):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM kategori WHERE kategori_id = %s",
                (kategori_id,)
            )
            conn.commit()
            conn.close()
        except Exception as e:
            print("ERROR DELETE:", e)




