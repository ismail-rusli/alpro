class Kas:
    def __init__ (self, _saldo):
        self.saldo = _saldo

    def uang_masuk (self, jumlah):
        self.saldo = self.saldo + jumlah

    def uang_keluar (self, jumlah):
        self.saldo = self.saldo - jumlah

    def get_saldo (self):
        return self.saldo

    def print_saldo (self):
        print("Saldo =", self.saldo)
