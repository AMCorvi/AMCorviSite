from django.db import models

# Create your models here.

# class Project(models.Model):
#     project_name = models.CharField(max_length=30)
#     img_url = models.URLField(max_length=50)
#     repo_url = models.URLField(max_length=50)
#     project_url = models.URLField(max_length=50)
#     description = models.CharField(max_length=300)
#
#     # 'technologies' is being used to make do as a tag. Note that it will take on the following format:
#     #  e.g. (" reactjs, nodejs, mocha, chai, python, django")
#     # This field should therefore be sorted using the 'str.split()' method.
#     technologies =  models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.project_name
