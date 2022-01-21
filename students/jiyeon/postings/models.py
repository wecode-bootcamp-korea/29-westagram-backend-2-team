from django.db import models
from django.db.models.deletion import CASCADE

class Posting(models.Model):
    user       = models.ForeignKey('users.User', on_delete=models.CASCADE) 
    img_url    = models.URLField()
    content    = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'postings'

class Comment(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    post = models.ForeignKey(Posting, on_delete=CASCADE)
    comment = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'comments'