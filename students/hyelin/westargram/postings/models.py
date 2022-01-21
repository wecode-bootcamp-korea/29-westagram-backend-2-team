from django.db import models
from users.models import User

class Board(models.Model):
    writer          = models.ForeignKey(User, on_delete = models.CASCADE)    
    content         = models.CharField(max_length = 300, blank=True)
    image_url       = models.URLField(blank=True)
    written_date    = models.DateTimeField(auto_now_add = True)
    updated_date    = models.DateTimeField(auto_now = True)
    
    class Meta :
        db_table='boards'