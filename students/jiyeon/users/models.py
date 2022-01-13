from django.db import models
from django.db.models.deletion import CASCADE


class User(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)

    class Meta:
        db_table = 'users'


