from django.db import models
from django.db.models.deletion import CASCADE
# Create your models here.

class Posting(models.Model):
    user        = models.ForeinKey('users.User', on_delete=models.CASADE)
    img_url     = models.UrlField()
    content     = models.CharField(max_length=1000)
    created_at  = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'postings'
