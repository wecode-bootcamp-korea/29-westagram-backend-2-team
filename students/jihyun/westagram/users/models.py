from django.db import models

# Create your models here.
class User(models.Model) :
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    email = models.ForeignKey(Email, on_delete=models.CASCADE)
    phonenumber = models.CharField(max_length=20)

    class Meta :
        db_table = 'users'
