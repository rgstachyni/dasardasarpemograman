from animal import *

class Ikan(animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, habitat, ukuran):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.habitat = habitat
        self.ukuran = ukuran
    def cetak_ikan(self):
        super().cetak()
        print("habitat \t: ", self.habitat, 
              "\nUkuran \t: ", self.ukuran)

Hiu = Ikan("Hiu", "Daging", "Laut", "Telur", "Laut", "Besar")
Hiu.cetak_ikan()
Mas= Ikan("Mas", "Pakan Ikan", "Air Tawar", "Telur", "Kolam", "Kecil")
Mas.cetak_ikan()