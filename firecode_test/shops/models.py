from django.db import models
from django.conf import settings
import peewee


db = settings.DATABASES['default']
database = peewee.PostgresqlDatabase(db['NAME'], user=db['USER'], password=db['PASSWORD'])


class BaseModel(peewee.Model):
    name = peewee.CharField()

    class Meta:
        database = database

    def __str__(self):
        return self.name


class PeeweeCity(BaseModel):
    id = peewee.PrimaryKeyField()
    name = peewee.CharField(max_length=255)

    class Meta:
        db_table = 'shops_city'


class PeeweeStreet(BaseModel):
    id = peewee.PrimaryKeyField()
    name = peewee.CharField(max_length=255)
    city = peewee.ForeignKeyField(PeeweeCity, backref='streets', on_delete='CASCADE')

    class Meta:
        db_table = 'shops_street'


class PeeweeShop(BaseModel):
    id = peewee.PrimaryKeyField()
    name = peewee.CharField(max_length=255)
    city = peewee.ForeignKeyField(PeeweeCity, backref='shops', on_delete='CASCADE')
    street = peewee.ForeignKeyField(PeeweeStreet, backref='shops', on_delete='CASCADE')
    building = peewee.CharField(max_length=10)
    opens = peewee.TimeField()
    closes = peewee.TimeField()

    class Meta:
        db_table = 'shops_shop'


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
