from django.db import models

 # Create your models here.
 class User(models.Model) :
     name        = models.CharField(max_length=50)
     email       = models.EmailField(Unique=True)
     password    = models.CharField(max_length=200)
     phonenumber = models.CharField(max_length=20)
     created_at  = models.DateTimeField(auto_now_add=True)
     updated_at  = models.DateTimeField(auto_now=True)

     class Meta :
         db_table = 'users'
