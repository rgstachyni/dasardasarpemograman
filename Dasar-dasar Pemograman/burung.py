from animal import *

class Burung(animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis, bunyi):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis = jenis
        self.bunyi = bunyi
    def cetak_burung(self):
        super().cetak()
        print("jenis \t: ", self.jenis, 
              "\nBunyi \t: ", self.bunyi)

Merpati = Burung("Merpati", "Biji-bijian", "Udara", "Telur", "Kolumbidae", "cooo-woook-woook")
Merpati.cetak_burung()
Gereja = Burung("Gereja", "Jagung", "Udara", "Telur", "Sparrow", "cicwit-cicwit")
Gereja.cetak_burung()