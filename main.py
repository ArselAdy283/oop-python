nama_wisata = "indomaret"

class Orang:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  def sapa(self):
    return "halo " + self.name
    
  def welcome(self):
    pesan = self.sapa()
    
    if (self.age < 18):
      print(pesan + ", kamu dilarang ke " + nama_wisata)
    else:
      print(pesan + ", Selamat datang di " + nama_wisata)
    
orang1 = Orang("Ega", 18)
orang1.welcome()
