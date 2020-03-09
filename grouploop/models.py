from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.


class User(AbstractUser):
    name = models.TextField(settings.AUTH_USER_MODEL, blank=True)
    github = models.TextField()
    facebook = models.TextField()
    instagram = models.TextField()
    linkedin = models.TextField()
    twitter = models.TextField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Circle(models.Model):
    title = twitter = models.TextField()
    description = models.TextField()
    member = models.ManyToManyField(User, settings.AUTH_USER_MODEL, blank=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
