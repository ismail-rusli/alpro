import random

class Papan:
    def __init__ (self, jumlah_kotak: int):
        self.jumlah_kotak = jumlah_kotak
        self.kotak = {}
        self.buat_papan()

    # TODO:
    # buatlah batasan untuk jumlah ular dan tangga,
    # misalnya ular 10% dari jumlah_kotak
    # dan tangga juga 10% dari jumlah kotak
    def buat_papan (self):
        for i in range(self.jumlah_kotak):
            self.kotak[i] = random.randint(-10,10)

    def print_kotak(self):
        print(self.kotak)

    def get_kotak(self, nomor:int):
        return self.kotak[nomor]

