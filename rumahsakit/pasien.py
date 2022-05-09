class Pasien:
    def __init__ (self, nomor: int, nama: str, alamat: str, umur: int, jenis_kelamin: bool):
        self.nomor = nomor
        self.nama = nama
        self.alamat = alamat
        self.umur = umur
        self.jenis_kelamin = jenis_kelamin

    def get_nomor (self):
        return self.nomor

    def get_nama (self):
        return self.nama

    def get_alamat (self):
        return self.alamat

    def get_umur (self):
        return self.umur

    def get_jenis_kelamin (self):
        return self.jenis_kelamin

    def set_nomor (self, nomor_baru: int):
        self.nomor = nomor_baru

    def set_nama (self, nama_baru: str):
        self.nama = nama_baru

    def set_alamat (self, alamat_baru: str):
        self.alamat = alamat_baru

    def set_umur (self, umur_baru: int):
        self.umur = umur_baru

    def set_jenis_kelamin (self, jenis_kelamin_baru: bool):
        self.jenis_kelamin = jenis_kelamin_baru
