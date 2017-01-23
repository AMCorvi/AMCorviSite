from django.db import models

# Create your models here.

class Tags(models.Model):
   tag_name = models.CharField(max_length=15)

class Blog(models.Model):
   post_title = models.CharField(max_length=50)
   post_content = models.TextField()
   date_create = models.DateTimeField('data published')
   img_url = models.CharField(max_length=300)
   tags = models.ManyToManyField(Tags)

