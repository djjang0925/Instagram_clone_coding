from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit import processors
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.


class User(AbstractUser):
    pass


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nickname = models.TextField(max_length=40)
    introduction = models.TextField()
    image = models.ImageField(blank=True)
    image_field = ImageSpecField(
        source='image',
        processors=[ResizeToFill(300, 300)],
        format="jpeg",
        options={'quality': 90},
    )
