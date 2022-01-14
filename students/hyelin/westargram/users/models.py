from pyexpat import model
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=300)
    phone = models.CharField(unique=True, max_length=120)

    class Meta :
        db_table = 'users'
