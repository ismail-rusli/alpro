from pasien import Pasien
from dokter import Dokter
from penyakit import Penyakit

class MedicalRecord:
    def __init__ (self, pasien: Pasien, dokter: Dokter, penyakit: Penyakit):
        self.pasien = pasien
        self.dokter = dokter
        self.penyakit = penyakit

