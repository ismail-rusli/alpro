import random

class Petarung:
    def __init__(self,nama):
        self.nama = nama
        self.kesehatan = 100
        self.kekuatan = random.randint(0,100)
        self.kecerdasan = random.randint(0,100)
        self.kelincahan = random.randint(0,100)
        self.senjata = random.randint(0,100)

    def cek_kesehatan(self): return self.kesehatan
    def cek_kekuatan(self): return self.kekuatan
    def cek_kecerdasan(self): return self.kecerdasan
    def cek_kelincahan(self): return self.kelincahan
    def cek_senjata(self): return self.senjata

    def print_data(self):
        print(self.nama)
        print("Kesehatan = " + str(self.kesehatan))
        print("Kekuatan = " + str(self.kekuatan))
        print("Kecerdasan = " + str(self.kecerdasan))
        print("Kelincahan = " + str(self.kelincahan))
        print("Senjata = " + str(self.senjata))
