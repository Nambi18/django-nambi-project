from django.db import models

# Create your models here.
class bookorder(models.Model):
    un = models.CharField(max_length=20)
    em = models.CharField(max_length=40)
    mss = models.CharField(max_length=60)