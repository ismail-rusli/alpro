from pasien import Pasien
from dokter import Dokter
from penyakit import Penyakit

class MedicalRecord:
    def __init__ (self, pasien: Pasien, dokter: Dokter, penyakit: Penyakit):
        self.pasien = pasien
        self.doketer = dokter
        self.penyakit = penyakit

    def get_pasien (self):
        return self.pasien

    def get_dokter (self):
        return self.dokter

    def get_penyakit (self):
        return self.penyakit

    def set_pasien (self, pasien: Pasien):
        self.pasien = pasien

    def set_dokter (self, dokter: Dokter):
        self.dokter = dokter

    def set_penyakit (self, penyakit: Penyakit):
        self.penyakit = penyakit

