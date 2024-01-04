from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=30)
    place = models.CharField(max_length=30)
    number = models.CharField(max_length=12)

    def __str__(self):
        return self.name
    