from django.db import models

# Create your models here.
class Airport(models.Model):
    pin = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.pin} ({self.city})"

class Students(models.Model):
    first = models.CharField(max_length=15)
    last = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first} {self.last}"


class Marks(models.Model):
    Math = models.IntegerField()
    Scinece = models.IntegerField()
    Language = models.IntegerField()
    name = models.ForeignKey(Students, on_delete=models.CASCADE, blank=True , related_name="name")

    def _str_(self):
        return f"{self.Math} {self.Science} {self.Language} {self.name}"
