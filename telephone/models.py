from django.db import models

# Create your models here.

class Telephone(models.Model):
    forename=models.CharField(max_length=25)
    surname=models.CharField(max_length=25)
    middle_name=models.CharField(max_length=25)
    phone_number=models.IntegerField(max_length=11, unique=True)
    gender=models.CharField(max_length=25)

def _str_(self):
    return self.forename