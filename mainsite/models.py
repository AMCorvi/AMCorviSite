from django.db import models

# Create your models here.

class Link(models.Model):
    name = models.CharField(max_length=30)
    url = models.URLField(max_length=50)
    description = models.CharField(max_length=300, blank=True)
    date = models.DateTimeField(blank=True, auto_now_add=True)

    def __str__(self):
        return self.name
