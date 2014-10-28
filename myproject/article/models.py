from django.db import models

class Article(models.Model):
    title = models.Charfield (max_length = 200)
    body = models.TextFeild()
    pub_date = models.DateTimeField('date published')
    likes = model.IntegerField()
    
