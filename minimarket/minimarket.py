from inventori import Inventori
from kas import Kas
from barang import Barang
from transaksi import Transaksi

inventori = Inventori()
kas = Kas(1000000)
transaksi = Transaksi (inventori, kas)

sabun = Barang ("sabun", 1000)
minyak = Barang ("minyak", 20000)
roti = Barang ("roti", 1000)
pensil = Barang ("pensil", 500)
sapu = Barang ("sapu", 15000)
pensil = Barang ("pensil", 500)

print("Beli barang")
print("----------")
transaksi.beli_barang (sabun, 10)
transaksi.beli_barang (minyak, 10)
transaksi.beli_barang (roti, 10)
transaksi.beli_barang (pensil, 10)
transaksi.beli_barang (sapu, 10)

print("")
inventori.print_inventori()

print("")
print("Jual barang")
print("----------")
transaksi.jual_barang (sabun, 5)
transaksi.jual_barang (minyak, 8)
transaksi.jual_barang (roti, 3)
transaksi.jual_barang (pensil, 1)

print("")
inventori.print_inventori()
