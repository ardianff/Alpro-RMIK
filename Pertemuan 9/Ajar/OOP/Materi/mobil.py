# Class mobil
class Mobil :
  def __init__(self,tipe,tahun,kecepatan) :
    self.tipe = tipe
    self.tahun = tahun
    self.kecepatan = kecepatan
    
  def doMelaju(self):
    print("Melaju dengan kecepatan : ",self.kecepatan, " Km/h")
  def doKlakson(self):
    print("Klakson")
  def doBelok(self,arah):
    print("Mobil berbelok kearah ", arah)
    
# Membuat instance object
mobilFerari = Mobil("Sport",2022,200)
mobilJeep = Mobil("Offroad",2021,150)

#akses dari setiap attribut
print("Mobil Ferari adalah mobil tipe ",mobilFerari.tipe," dan diproduksi tahun",mobilFerari.tahun)
print("Mobil Jeep tipe adalah mobil tipe",mobilJeep.tipe)

# mengakses method yang sudah didefinisikan di dalam class Mobil
mobilFerari.doMelaju()
mobilJeep.doMelaju()

# mengakses method 
mobilFerari.doBelok("Kanan")
mobilJeep.doBelok("Kanan")