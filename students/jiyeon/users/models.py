from django.db import models

class User(models.Model):
    name         = models.CharField(max_length=30)
    email        = models.CharField(max_length=200, unique=True)
    password     = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=30)
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users'