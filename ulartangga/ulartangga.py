from papan import Papan
from pion import Pion
import random

def lempar_dadu():
    return random.randint(0,6)

papan = Papan(101)
pion1 = Pion("budi")
pion2 = Pion("wati")

print("Permainan Ular Tangga")
print(pion1.get_nama(), "sekarang berada di posisi", pion1.get_posisi())
print(pion2.get_nama(), "sekarang berada di posisi", pion2.get_posisi())

iterasi = 0
posisi1 = pion1.get_posisi()
posisi2 = pion2.get_posisi()

while posisi1 < 100 and posisi2 < 100:
    dadu1 = lempar_dadu()
    dadu2 = lempar_dadu()
    posisi1 = posisi1 + dadu1
    posisi2 = posisi2 + dadu2

    if (posisi1 > 100 or posisi2 > 100):
        break

    if (posisi1 < 0 or posisi2 < 0):
        posisi1 = 0
        posisi2 = 0

    kotak1 = papan.get_kotak (posisi1)
    kotak2 = papan.get_kotak (posisi2)

    posisi1 = posisi1 + kotak1
    posisi2 = posisi2 + kotak2
    if (posisi1 < 0): posisi1 = 0
    if (posisi2 < 0): posisi2 = 0
    pion1.set_posisi (posisi1)
    pion2.set_posisi (posisi2)

    iterasi = iterasi + 1

    print("Iterasi ke ", iterasi)
    pion1.print_posisi()
    pion2.print_posisi()

    if (iterasi > 100):
        break

if (posisi1 > posisi2) and posisi1 >= 100:
    print("Pemenangnya adalah", pion1.get_nama())
elif (posisi1 < posisi2) and posisi2 >= 100:
    print("Pemenangnya adalah", pion2.get_nama())
else:
    print("Tidak ada pemenang")
