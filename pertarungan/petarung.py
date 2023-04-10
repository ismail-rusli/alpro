import random
import os

class Petarung:
    def __init__ (self, nama_petarung: str):
        self.nama = nama_petarung
        self.kesehatan = 100
        self.kekuatan = random.randint (0,100)
        self.kecerdasan = random.randint (0,100)
        self.kelincahan = random.randint (0,100)
        self.senjata = random.randint (0,100)
        self.skor = 0
        self.menang = 0
        self.kalah = 0
        self.seri = 0

    def print_data (self):
        print ("===== ", self.nama, "==========")
        print ("Kesehatan = ", self.kesehatan)
        print ("Kekuatan = ", self.kekuatan)
        print ("Kecerdasan = ", self.kecerdasan)
        print ("Kelincahan = ", self.kelincahan)
        print ("Senjata = ", self.senjata)

    def regenerate(self):
        self.kesehatan = self.kesehatan - 5
        self.kekuatan = random.randint (0,100)
        self.kecerdasan = random.randint (0,100)
        self.kelincahan = random.randint (0,100)
        self.senjata = random.randint (0,100)

    def edit (self, nama_baru):
        nama_lama = self.nama
        self.nama = nama_baru

class DB_Petarung:
    def __init__ (self, namafile):
        self.db_path = namafile
        self.db_dir = namafile.split('/')[0]
        self.db_file = namafile.split('/')[1]
        self.data = []
        self.load()

    def load (self):
        if not os.path.isdir (self.db_dir):
            os.mkdir (db_dir)

        if not os.path.exists (self.db_path):
            f = open (self.db_path, 'x')
            f.close()

        f = open (self.db_path, 'r')
        for x in f:
            file_petarung = self.db_dir + "/" + x.strip() + '.txt'
            petarung = Petarung (x.strip())
            if os.path.exists (file_petarung):
                g = open (file_petarung, 'r')
                g.readline().strip() # skip nama
                petarung.nama = x.strip()
                petarung.kesehatan = int (g.readline().strip())
                petarung.kekuatan = int (g.readline().strip())
                petarung.kecerdasan = int (g.readline().strip())
                petarung.kelincahan = int (g.readline().strip())
                petarung.senjata = int (g.readline().strip())
                self.data.append (petarung)
                g.close()
            else:
                self.write_petarung_to_file (petarung)

    def print_all_petarung (self):
        for petarung in self.data:
            petarung.print_data()

    def print_nama_petarung (self):
        print ("==== Dafta nama petarung =====")
        for petarung in self.data:
            print (petarung.nama)
        print ("==============================")

    def edit (self, nama_lama, nama_baru):
        file_lama = self.db_dir + '/' + nama_lama + ".txt"
        file_baru = self.db_dir + '/' + nama_baru + ".txt"

        for petarung in self.data:
            if nama_lama == petarung.nama:
                petarung.edit (nama_baru)
                self.write_petarung_to_file (petarung)
                os.remove (file_lama)
                break

        f = open (self.db_path, 'w')
        for petarung in self.data:
            f.writelines (petarung.nama + '\n')
        f.close()

    def add_petarung (self, nama):
        if self.petarung_exists (nama):
            print ("Nama petarung sudah ada")
        else:
            petarung = Petarung (nama)
            self.data.append (petarung)
            self.write_petarung_to_file (petarung)
            self.write_db_to_file ()

    def write_petarung_to_file(self, petarung):
        namafile = self.db_dir + '/' + petarung.nama + '.txt'
        f = open (namafile, 'w')
        f.writelines (petarung.nama + '\n')
        f.writelines (str(petarung.kesehatan) + '\n') 
        f.writelines (str(petarung.kekuatan) + '\n') 
        f.writelines (str(petarung.kecerdasan) + '\n') 
        f.writelines (str(petarung.kelincahan) + '\n') 
        f.writelines (str(petarung.senjata) + '\n') 
        f.close()

    def write_all_petarung_to_file (self):
        for petarung in self.data:
            self.write_petarung_to_file (petarung)

    def write_db_to_file (self):
        if not os.path.exists (self.db_path):
            f = open (self.db_path, 'x')
            f.close()

        f = open (self.db_path, 'w')
        for petarung in self.data:
            f.writelines (petarung.nama + '\n')
        f.close()

    def petarung_exists (self, nama):
        petarung = self.get_petarung (nama)
        if petarung: 
            return True
        return False

    def del_petarung (self, nama):
        petarung = self.get_petarung (nama)
        if petarung: 
            self.data.remove (petarung)
            self.write_db_to_file()
            os.remove (self.db_dir + '/' + nama + '.txt')
        else:
            print ("Petarung tidak ada")

    def get_petarung (self, nama):
        for petarung in self.data:
            if petarung.nama == nama:
                return petarung








