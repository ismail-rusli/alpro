class Tanding:
    def __init__(self, petarung1, petarung2):
        self.petarung1 = petarung1
        self.petarung2 = petarung2
        self.pemenang = ""

    def mulai(self):
        """ 
        pemenang pertarungan ditentukan dengan cara sbb.
        setiap sifat antara 2 petarung dibandingkan
        yang lebih besar mendapatkan 1 point.
        pemenang adalah petarung yang memiliki
        point paling besar.
        """
        nilai_petarung1 = 0
        nilai_petarung2 = 0

        if (self.petarung1.kekuatan > self.petarung2.kekuatan):
            nilai_petarung1 = nilai_petarung1 + 1
        elif (self.petarung1.kekuatan < self.petarung2.kekuatan):
            nilai_petarung2 = nilai_petarung2 + 1

        # dan seterusnya untuk kecerdasan, kelincahan,
        # dan juga senjata

        if (nilai_petarung1 > nilai_petarung2):
            self.pemenang = self.petarung1.nama
        elif (nilai_petarung1 < nilai_petarung2):
            self.pemenang = self.petarung2.nama
        else:
            self.pemenang = ""

    def print_pemenang(self):
        if (self.pemenang != ""):
            print("Pemenangnya: " + self.pemenang)
        else:
            print("Seri!!")
        
