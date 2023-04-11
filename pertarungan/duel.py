import os
from petarung import *
from pertandingan import Pertandingan
from menu import Menu

namafile = "data/db_petarung.txt"
db_petarung = DB_Petarung (namafile)

menu = ['1. Lihat petarung', 
        '2. Edit petarung',
        '3. Tambah petarung',
        '4. Hapus petarung',
        '5. Bertanding',
        '6. Keluar']

app_menu = Menu (menu)

while True:
    os.system('clear')
    app_menu.print_menu()

    pilihan = input ("Pilihan ")

    if pilihan == '1':
        db_petarung.print_all_petarung()
    elif pilihan == '2':
        db_petarung.print_nama_petarung()
        nama_lama = input ("Siapa petarung yang akan diedit? ")
        if db_petarung.petarung_exists(nama_lama):
            nama_baru = input ("Siapa nama baru petarung? ")
            if not db_petarung.petarung_exists (nama_baru):
                db_petarung.edit (nama_lama, nama_baru)
            else:
                print ("Nama petarung sudah ada")
        else:
            print ("Nama tidak ada")
    elif pilihan == '3':
        nama = input ("Siapa nama petarung: ")
        db_petarung.add_petarung (nama)
    elif pilihan == '4':
        db_petarung.print_nama_petarung()
        nama_hapus = input ("Nama petarung yang akan dihapus? ")
        if db_petarung.petarung_exists (nama_hapus):
            db_petarung.del_petarung (nama_hapus)
        else:
            print ("Nama tidak ada")
    elif pilihan == '5':
        db_petarung.print_nama_petarung()
        petarung1, petarung2 = None, None
        while not petarung1: 
            nama1 = input ("Nama petarung 1: ")
            if db_petarung.petarung_exists (nama1):
                petarung1 = db_petarung.get_petarung (nama1)
            else:
                print ("Nama tidak ada")

        while not petarung2: 
            nama2 = input ("Nama petarung 2: ")
            if db_petarung.petarung_exists (nama2):
                petarung2 = db_petarung.get_petarung (nama2)
            else:
                print ("Nama tidak ada")

        pertandingan = Pertandingan (petarung1, petarung2)
        pertandingan.mulai()
        pertandingan.print_pemenang()

        for petarung in db_petarung.data:
            if petarung != petarung1 and petarung != petarung2:
                petarung.kesehatan += 3

        db_petarung.write_all_petarung_to_file()

    elif pilihan == '6':
        print ("Sampai jumpa")
        break

    input ("Tekan enter untuk melanjutkan.")
