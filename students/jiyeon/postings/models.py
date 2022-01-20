class Comment(models.Model):
    user         = models.ForeignKey('users.User', on_delete=models.CASCADE)
    post         = models.ForeignKey('Posting', on_delete=models.CASCADE)
    comment      = models.Charfield(max_length=1000)
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'comments'