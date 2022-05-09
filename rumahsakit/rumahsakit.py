from pasien import Pasien
from dokter import Dokter
from penyakit import Penyakit
from medrecord import MedicalRecord
from database_pasien import DbPasien


db_pasien = DbPasien()
run = True

print ("Selamat datang di aplikasi Rumah Sakit.")
print ("--------------------------------------")

while (run):
    print ("Silakan pilih menu berikut.")
    print ("1. Kelola data pasien")
    print ("2. Kelola data dokter")
    print ("3. ...")
    print ("4. Keluar")
    pilihan = input ("Silakan masukkan pilihan Anda (1/2/3/4): ")
    print ("")
    if pilihan == '1':
        db_pasien.run_menu()
    elif pilihan == '2':
        print ("Menu ini belum diimplementasikan.")
    elif pilihan == '3':
        print ("Menu ini belum diimplementasikan.")
    elif pilihan == '4':
        print ("Terima kasih")
        run = False
    else:
        print ("Anda tidak memasukkan pilihan dengan benar.")
    print ("")

