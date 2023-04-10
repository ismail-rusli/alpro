class Barang:
    def __init__ (self, _merk, _harga):
        self.merk = _merk
        self.harga = _harga

    def print_data(self):
        print("Nama: ", self.merk)
        print("Harga = ", self.harga)
        print("----------")
        
