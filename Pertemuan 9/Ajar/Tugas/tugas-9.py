
class Pemeriksaan :
  def __init__(self,nama,diastolik,sistolik,berat, tinggi) :
    self.nama = nama
    self.diastolik = diastolik
    self.sistolik = sistolik
    self.berat = berat
    self.tinggi = tinggi
  def cektensi(self) :
    print("Tekanan darah ",self.nama,"sebesar ",self.diastolik,"/",self.sistolik)
  def ceksaturasi(self,saturasi):
    if(saturasi>= 95):
      print("Halo ",self.nama," saturasi oksigen anda normal")
    else:
      print("Halo ",self.nama," saturasi oksigen anda rendah")
  def cekbmi(self):
    tinggimeter = self.tinggi/100
    tinggibadan = pow(tinggimeter,2)
    bmipasien = self.berat/tinggibadan
    
    if(bmipasien>=30):
      print("Halo ",self.nama,"berat badan kamu",self.berat,"dan tinggi kamu ",self.tinggi," dengan BMI ",bmipasien," termasuk kategori Obesitas. Yuk olahraga dan hidup sehat\n")
    elif(bmipasien>=23 or bmipasien == 29.9):
      print("Halo ",self.nama," Berat badan kamu ",self.berat,"dan tinggi kamu ",self.tinggi," dengan BMI ",bmipasien," termasuk kategori berlebih. Yuk olahraga dan hidup sehat\n")
    elif(bmipasien>=18.5 or bmipasien == 22.9):
      print("Halo ",self.nama," Berat badan kamu ",self.berat,"dan tinggi kamu ",self.tinggi," dengan BMI ",bmipasien," termasuk kategori normal. Tetap jaga kesehatan ya\n")
    else:
      print("Halo ",self.nama," Berat badan kamu ",self.berat,"dan tinggi kamu ",self.tinggi," dengan BMI ",bmipasien," termasuk kategori kurang proposional. Penuhi kecukupan gizi tubuh anda dengan makan makanan bergizi dan olahraga yang cukup ya\n")
      
pasien1 = Pemeriksaan("Arifin",90,130,100,168)
    
pasien1.cektensi()
pasien1.ceksaturasi(99)
pasien1.cekbmi()

  
    
    
  
    