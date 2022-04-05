class Transaksi:
    def __init__ (self, _inventori, _kas):
        self.inventori = _inventori
        self.kas = _kas

    def jual_barang (self, barang, jumlah):
        self.inventori.kurangi_inventori(barang, jumlah)
        self.kas.uang_masuk (barang.get_harga() * jumlah)
        print(  "Penjualan",
                barang.get_merk(), 
                "sebanyak", 
                jumlah, 
                "berhasil", 
                end = " --> ")
        self.kas.print_saldo()

    def beli_barang(self, barang, jumlah):
        self.inventori.tambah_inventori (barang, jumlah)
        self.kas.uang_keluar (barang.get_harga() * jumlah)
        print(  "Pembelian", 
                barang.get_merk(), 
                "sebanyak", 
                jumlah, 
                "berhasil", 
                end = " --> ")
        self.kas.print_saldo()

