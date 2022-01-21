from django.db import models
from users.models import User

class Post(models.Model):
    title           = models.CharField(max_length = 200)
    writer          = models.ForeignKey(User, on_delete = models.CASCADE)    
    content         = models.CharField(max_length = 300)
    written_date    = models.DateTimeField(auto_now_add = True)
    updated_date    = models.DateTimeField(auto_now = True)
    
    class Meta :
        db_table='posts'

class PostImage(models.Model) :
    post_id         = models.ForeignKey(Post, on_delete= models.CASCADE)
    img_url         = models.URLField(max_length= 200, blank= False)
    uproaded_date   = models.DateTimeField(auto_now_add= True)

    class Meta :
        db_table = 'postimages'
