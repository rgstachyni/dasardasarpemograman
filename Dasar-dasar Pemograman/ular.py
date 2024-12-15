from animal import *

class Ular(animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, design, racun):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.design = design
        self.racun = racun
    def cetak_ular(self):
        super().cetak()
        print("Design \t: ", self.design, 
              "\nRacun \t: ", self.racun)

anaconda = Ular("Anaconda", "Kambing", "Amazon", "Bertelur", "Batik Solo", "Tidak Berbisa")
anaconda.cetak_ular()
Kobra = Ular("Kobra", "Tikus", "Hutan", "Bertelur", "Batik Jogjga", "Berbisa")
Kobra.cetak_ular()