from xml.dom.pulldom import PROCESSING_INSTRUCTION


class Pion:
    def __init__(self, nama: str):
        self.nama = nama
        self.posisi = 0

    def set_posisi (self, posisi: int):
        self.posisi = posisi

    def get_posisi (self):
        return self.posisi

    def print_posisi (self):
        print ("Posisi pion", self.nama, "sekarang adalah ", self.posisi)

    def get_nama (self):
        return self.nama