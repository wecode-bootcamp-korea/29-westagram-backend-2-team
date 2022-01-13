from django.db import models

# Create your models here.
class Name(models.Model) :
    name = models.CharField(max_length=50)

    class Meta :
        db_table = 'names'

class Email(models.Model) :
    address = models.CharField(max_length=100)
    name = models.ForeignKey(Name, on_delete=models.CASCADE)

    class Meta :
        db_table = 'emails'

class Password(models.Model) :
    password = models.CharField(max_length=20)
    email = models.ForeignKey(Email, on_delete=models.CASCADE)

    class Meta :
        db_table = 'passwords'

class Phonenumber(models.Model) :
    phonenumber = models.CharField(max_length=20)
    name = models.ForeignKey(Name, on_delete=models.CASCADE)

    class Meta :
        db_table = 'phonenumbers'
