class Transaksi:
    def __init__ (self, inventori, kas):
        self.inventori = inventori
        self.kas = kas

    def jual_barang (self, barang, jumlah):
        self.inventori.kurangi_inventori(barang, jumlah)
        self.kas.saldo += barang.harga * jumlah
        print(  "Penjualan",
                barang.merk,
                "sebanyak", 
                jumlah, 
                "berhasil", 
                end = " --> ")
        self.kas.print_saldo()

    def beli_barang(self, barang, jumlah):
        self.inventori.tambah_inventori (barang, jumlah)
        self.kas.saldo -= barang.harga * jumlah
        print(  "Pembelian", 
                barang.merk,
                "sebanyak", 
                jumlah, 
                "berhasil", 
                end = " --> ")
        self.kas.print_saldo()

