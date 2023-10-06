from django.db import models

# Create your models here.
class Post(models.Model):
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)