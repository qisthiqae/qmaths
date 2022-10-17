from django.db import models

# Create your models here.
class Visitor(models.Model):
    Nama = models.TextField()
    Nomorhp = models.CharField(max_length=20)
    Email = models.TextField()
    Pekerjaan = models.TextField()
    Domisili = models.TextField()
 
    def _str_(self):
        return self.Nama