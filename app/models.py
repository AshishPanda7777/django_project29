from django.db import models

# Create your models here.
class College(models.Model):
    Cname=models.CharField(max_length=100)
    Cprincipal=models.CharField(max_length=100)
    Cloaction=models.CharField(max_length=100)