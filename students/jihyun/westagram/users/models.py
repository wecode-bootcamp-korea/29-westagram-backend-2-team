from django.db import models

# Create your models here.
class User(models.Model) :
    name        = models.CharField(max_length=50)
    address     = models.EmailField(Unique=True)
    password    = models.CharField(max_length=200)
    phonenumber = models.CharField(max_length=20)

    class Meta :
        db_table = 'users'
