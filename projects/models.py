from django.db import models
from django.utils.safestring import mark_safe
from PIL import Image

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)


    def __str__(self):
        return self.title


