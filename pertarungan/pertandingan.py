import random
from petarung import Petarung

class Pertandingan:
    def __init__ (self, petarung1, petarung2):
        self.petarung1 = petarung1
        self.petarung2 = petarung2
        self.pemenang = ''

    def mulai(self):
        nilai_petarung1 = 0
        nilai_petarung2 = 0

        if self.petarung1.kekuatan > self.petarung2.kekuatan:
            nilai_petarung1 = nilai_petarung1 + 1
        elif self.petarung2.kekuatan > self.petarung1.kekuatan:
            nilai_petarung2 = nilai_petarung2 + 1

        if self.petarung1.kecerdasan > self.petarung2.kecerdasan:
            nilai_petarung1 = nilai_petarung1 + 1
        elif self.petarung2.kecerdasan > self.petarung1.kecerdasan:
            nilai_petarung2 = nilai_petarung2 + 1

        if self.petarung1.kelincahan > self.petarung2.kelincahan:
            nilai_petarung1 = nilai_petarung1 + 1
        elif self.petarung2.kelincahan > self.petarung1.kelincahan:
            nilai_petarung2 = nilai_petarung2 + 1

        if self.petarung1.senjata > self.petarung2.senjata:
            nilai_petarung1 = nilai_petarung1 + 1
        elif self.petarung2.senjata > self.petarung1.senjata:
            nilai_petarung2 = nilai_petarung2 + 1

        if nilai_petarung1 > nilai_petarung2:
            self.pemenang = self.petarung1.nama
            self.petarung2.kesehatan = self.petarung2.kesehatan - 5
            self.petarung1.kekuatan = self.petarung1.kekuatan + random.randint (1,5)
        elif nilai_petarung2 > nilai_petarung1:
            self.pemenang = self.petarung2.nama
            self.petarung1.kesehatan = self.petarung1.kesehatan - 5
            self.petarung2.kekuatan = self.petarung2.kekuatan + random.randint (1,5)
        else:
            self.pemenang = ""

        self.petarung1.regenerate()
        self.petarung2.regenerate()

    def print_pemenang (self):
        if self.pemenang != '':
            print ("Pemenangnya adalah ", self.pemenang)
        else:
            print ("Seri!")
