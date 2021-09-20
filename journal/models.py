from django.db import models

# Create your models here.


class Resourcelist(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField()
    resource_description = models.TextField()


