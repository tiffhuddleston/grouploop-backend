from django.db import models


# Create your models here.


class Member(models.Model):
    name = models.TextField()
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
    title = models.TextField()
    description = models.TextField()
    member = models.ManyToManyField(Member)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
