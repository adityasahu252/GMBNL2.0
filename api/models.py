from django.db import models

# Create your models here.
class Coustmer(models.Model):
    name=models.CharField(max_length=50)
    phone_number=models.IntegerField()
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=100)
    


    