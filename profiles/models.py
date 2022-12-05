from django.db import models
from django.core.exceptions import ValidationError


class Profiles(models.Model):
    name = models.CharField(unique=True, max_length=50)
    email = models.EmailField()
    age = models.IntegerField(null=True, blank=True)

    def clean(self):
        if self.age < 18:
            raise ValidationError("you don't have the access ")

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    profile = models.ForeignKey('profiles', on_delete=models.CASCADE, related_name='articles')

    def __str__(self):
        return self.title
