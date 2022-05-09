class Dokter:
    def __init__ (self, nomor: int, nama: str, spesialisasi: str):
        self.nomor = nomor
        self.nama = nama
        self.spesialisasi = spesialisasi

    def get_nomor (self):
        return self.nomor

    def get_nama (self):
        return self.nama

    def get_spesialisasi (self):
        return self.spesialisasi

    def set_nomor (self, nomor_baru: int):
        self.nomor = nomor_baru

    def set_nama (self, nama_baru: str):
        self.nama = nama_baru

    def set_spesialisasi (self, spesialisasi_baru: str):
        self.spesialisasi = spesialisasi_baru
