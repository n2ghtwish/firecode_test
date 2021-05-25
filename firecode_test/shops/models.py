from django.db import models


# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Street(models.Model):
    name = models.CharField(max_length=255)
    city = models.ForeignKey('City', related_name='streets', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Shop(models.Model):
    name = models.CharField(max_length=255)
    city = models.ForeignKey('City', related_name='shops', on_delete=models.CASCADE)
    street = models.ForeignKey('Street', related_name='shops', on_delete=models.CASCADE)
    building = models.CharField(max_length=10)
    opens = models.TimeField()
    closes = models.TimeField()

    def __str__(self):
        return self.name
