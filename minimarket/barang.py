class Barang:
    def __init__ (self, _merk, _harga):
        self.merk = _merk
        self.harga = _harga

    def ubah_merk (self, merk_baru):
        self.merk = merk_baru

    def ubah_harga (self, harga_baru):
        self.harga = harga_baru

    def get_merk (self):
        return self.merk

    def get_harga (self):
        return self.harga

    def print_data(self):
        print("Nama: ", self.merk)
        print("Harga = ", self.harga)
        print("----------")
        
