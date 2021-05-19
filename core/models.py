from django.db import models

# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=100)
    mail=models.EmailField()
    balance=models.FloatField(default=0)

class History(models.Model):
    transferto=models.CharField(max_length=100)
    transferby=models.CharField(max_length=100)
    amount=models.FloatField(default=0)
