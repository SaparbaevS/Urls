from django.db import models

class Sneakers(models.Model):
    name = models.CharField(max_length=20)
    size = models.IntegerField()
    price = models.IntegerField()


    def __str__(self):
        return f'{self.id} - {self.name} - {self.price}'


class Tshirts(models.Model):
    name = models.CharField(max_length=50)
    size = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return f"{self.id} - {self.name} - {self.price}"


class Souvenirs(models.Model):
    items = models.CharField(max_length=50)
    look_prints = models.CharField(max_length=50)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.id} - {self.items} - {self.price}"

