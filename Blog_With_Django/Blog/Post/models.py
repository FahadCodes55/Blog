from django.db import models
from django.utils import timezone


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now, blank=True)
    post_image = models.ImageField(upload_to='posts/')

