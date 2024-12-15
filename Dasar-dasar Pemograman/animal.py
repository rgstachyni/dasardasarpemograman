class animal:
    def __init__(self, nama, makanan, hidup, berkembang_biak):
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak
    def cetak(self):
        print("Nama \t\t: ", self.nama,
              "\makanan \t\t: ", self.makanan,
              "\hidup \t\t: ", self.hidup,
              "\berkembang_biak \t\t: ", self.berkembang_biak
              )
        
object = animal("buaya", "Daging", "Amphibi", "bertelur")
print(object.cetak())