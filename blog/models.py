from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tag(models.Model):
   tag_name = models.CharField(max_length=15)

   def __str__(self):
       return self.tag_name

class Blog(models.Model):
   author = models.CharField(max_length=20, blank=True)
   post_title = models.CharField(max_length=50)
   post_content = models.TextField()
   date_created = models.DateTimeField(auto_now_add=True)
   img_url = models.URLField(max_length=300, blank=True)
   publish = models.BooleanField(default=True)
   tags = models.ManyToManyField(Tag)

   def __str__(self):
      return self.post_title

