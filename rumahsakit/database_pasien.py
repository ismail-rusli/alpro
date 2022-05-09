from pasien import Pasien

class DbPasien:
    def __init__ (self):
        self.db_pasien = []
        self.menu_pasien = ['Print data pasien', 'Tambah data pasien', 'Cari data pasien', 'Hapus data pasien', 'Edit data pasien', 'Keluar']

    def run_menu (self):
        print ("Selamat datang di menu data pasien.")
        print ("-----------------------------------")
        pilihan = 1
        while (pilihan != 6):
            nomor = 1
            for menu in self.menu_pasien:
                print (nomor, menu)
                nomor += 1
            pilihan = int (input ("Silakan masukkan pilihan Anda: "))
            if pilihan == 1:
                print ("Anda memilih menu print data pasien.")
                nama = input ("Silakan tuliskan nama pasiennya: ")
                self.print_data_pasien_by_nama (nama)
            elif pilihan == 2:
                print ("Anda memilih menu tambah data pasien.")
                print ("Silakan isi data pasien baru berikut.")
                nama = input ("Nama: ")
                sudah_ada = self.cari_data_pasien_by_nama (nama)
                if sudah_ada != None:
                    print ("Nama pasien sudah terdaftar di database.")
                    return
                alamat = input ("Alamat: ")
                umur = int (input ("Umur: "))
                jenis_kelamin = input ("Jenis kelamin (L/P): ")
                jk = None
                if jenis_kelamin == 'L' or 'l':
                    jk = 1
                elif jenis_kelamin == 'P' or 'p':
                    jk = 0
                nomor = len(self.db_pasien) + 1
                pasien = Pasien (nomor = nomor, nama = nama, alamat = alamat, umur = umur, jenis_kelamin = jk)
                self.tambah_data_pasien (pasien)
            elif pilihan == 3:
                print ("Anda memilih menu cari data pasien.")
                nama = input ("Silakan masukkan nama pasien yang dicari: ")
                pasien = self.cari_data_pasien_by_nama (nama)
                if pasien == None:
                    print ("Data pasien dengan nama", nama, "tidak ditemukan.")
                else:
                    self.print_data_pasien_by_nama (nama)
            elif pilihan == 4:
                print ("Anda memilih menu hapus data pasien.")
                nama = input ("Silakan masukkan nama pasien yang akan dihapus datanya: ")
                self.hapus_data_pasien_by_nama (nama)
            elif pilihan == 5:
                print ("Anda memilih menu edit data pasien.")
                nama = input ("Silakan masukkan nama pasien yang akan diedit: ")
                self.edit_data_pasien_by_nama (nama)
            elif pilihan == 6:
                print ("Anda keluar dari menu data pasien. Terima kasih.")
            else:
                print ("Anda tidak memasukkan pilihan dengan benar")

            print ("")

    def print_data_pasien_by_nama (self, nama: str):
        for pasien in self.db_pasien:
            if pasien.get_nama() == nama:
                print ("Berikut adalah data pasien:")
                print ("Nama:", pasien.get_nama())
                print ("Umur:", pasien.get_umur())
                print ("Alamat:", pasien.get_alamat())
                if pasien.get_jenis_kelamin() == 1:
                    print ("Jenis kelamin: laki-laki")
                elif pasien.get_jenis_kelamin() == 0:
                    print ("Jenis kelamin: perempuan")
                else:
                    print ("Data jenis kelamin tidak tersedia.")
                return

        print ("Data pasien tidak ditemukan.")

    def tambah_data_pasien (self, pasien: Pasien):
        if pasien in self.db_pasien:
            print ("Pasien sudah ada dalam database.")
        else:
            self.db_pasien.append (pasien)
            print ("Pasien dengan nama", pasien.get_nama(), "berhasil disimpan.")

    def cari_data_pasien_by_nama (self, nama: str):
        for pasien in self.db_pasien:
            if pasien.get_nama() == nama:
                return pasien

        return None

    def hapus_data_pasien_by_nama (self, nama: str):
        for pasien in self.db_pasien:
            if pasien.get_nama() == nama:
                self.db_pasien.remove (pasien)
                print("Data pasien dengan nama", pasien.get_nama(), "telah dihapus.")
                break # break untuk keluar dari loop karena nama pasien sudah ditemukan

        print ("Pasien dengan nama", nama, "tidak terdaftar dalam database.")

    def edit_data_pasien_by_nama (self, nama: str):
        for pasien in self.db_pasien:
            if pasien.get_nama() == nama:
                print ("Pasien dengan nama", nama, "ditemukan.")
                edit = True
                while (edit):
                    print ("Pilih data yang akan diedit:")
                    print ("1. Nama")
                    print ("2. Alamat")
                    print ("3. Umur")
                    print ("4. Jenis kelamin")
                    pilih = input ("Silakan pilih (1/2/3/4): ")
                    if pilih == '1':
                        nama_baru = input ("Silakan masukan nama baru pasien: ")
                        pasien.set_nama (nama_baru)
                    elif pilih == '2':
                        alamat_baru = input ("Silakan masukan alamat baru pasien: ")
                        pasien.set_alamat (alamat_baru)
                    elif pilih == '3':
                        umur_baru = input ("Silakan masukan umur baru pasien: ")
                        pasien.set_umur (umur_baru)
                    elif pilih == '4':
                        jk = input ("Jenis kelamin pasien (L/P): ")
                        if jk == 'L':
                            pasien.set_jenis_kelamin (True)
                        elif jk == 'P':
                            pasien.set_jenis_kelamin (False)
                        else:
                            print ("Anda tidak memasukkan data dengan benar.")
                            print ("Jenis kelamin pasien tidak berubah.")
                    else:
                        print ("Anda tidak memasukkan pilihan dengan benar.")
                        print ("Data pasien tidak berubah.")

                    masih_edit = input ("Apakah Anda masih ingin meng-edit data pasien? (Y/T): ")
                    if masih_edit == 'T' or masih_edit == 't':
                        edit = False
                        print ("Edit data pasien selesai.")
                        self.print_data_pasien_by_nama (pasien.get_nama())
                    elif masih_edit == 'Y' or masih_edit == 'y':
                        pass
                    else:
                        edit = False
                        print ("Anda tidak memasukkan pilihan dengan benar.")
                        print ("Edit selesai")
