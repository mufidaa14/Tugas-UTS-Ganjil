from django.db import models

class Mata_kuliah(models.Model):
  hari = models.CharField(max_length=255)
  makul = models.CharField(max_length=255)
  jumlah_sks = models.CharField(max_length=2)

  def __str__(self):
    return f"{self.hari}"
  
class Mahasiswa(models.Model):
  Mata_kuliah = models.ForeignKey(Mata_kuliah, on_delete=models.CASCADE)
  nama = models.CharField(max_length=255)
  NPM = models.CharField(max_length=255)
  Prodi = models.CharField(max_length=255)

  def __str__(self):
    return f"{self.nama}"
  
# Create your models here.
