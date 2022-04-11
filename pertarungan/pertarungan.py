from petarung import Petarung
from tanding import Tanding

naruto = Petarung("Naruto")
sasuke = Petarung("Sasuke")
berantem = Tanding(naruto, sasuke)
berantem.mulai()

print("--------------------")
naruto.print_data()
print("--------------------")
sasuke.print_data()
print("--------------------")
berantem.print_pemenang()
print("--------------------")

print("Selesai")

