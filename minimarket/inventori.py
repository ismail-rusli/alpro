class Inventori:
    def __init__ (self):
        self.inventori = {} # tipe data dictionary

    def tambah_inventori (self, barang, jumlah):
        merk = barang.get_merk()
        jumlah_awal = 0

        # cek apakah barang sudah ada di inventori
        if merk in self.inventori.keys():
            jumlah_awal = self.inventori[merk]

        self.inventori[merk] = jumlah_awal + jumlah

    def kurangi_inventori (self, barang, jumlah):
        merk = barang.get_merk()
        jumlah_awal = 0

        # cek jumlah awal di inventori
        if merk in self.inventori.keys():
            jumlah_awal = self.inventori[merk]

        self.inventori[merk] = jumlah_awal - jumlah

    def print_inventori (self):
        print ("Inventori saat ini")
        print ("----------")
        for key,value in self.inventori.items():
            print("Merk =", key, ", Jumlah =", value)
        print("----------")

