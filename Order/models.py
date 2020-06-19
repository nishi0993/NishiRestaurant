from django.db import models
from django.utils import timezone

class Publications (models.Model):
    title = models.CharField(max_length=255)
    # class Meta:
    #     ordering = ['title']
    def __str__(self):
        return self.title


class Article(models.Model):
    headline = models.CharField(max_length=255)
    publications = models.ManyToManyField(Publications)
    # class Meta:
    #     ordering = ['headline']
    def __str__(self):
        return self.headline

class Place(models.Model):
    name = models.CharField(max_length=255)
    adress = models.TextField()
    def __str__(self):
        return self.name

class Restaurant(models.Model):
    place = models.OneToOneField(Place, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name


class Staff(models.Model):
    name = models.CharField(max_length=255)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    designation = models.CharField(max_length=255)
    def __str__(self):
        return self.name

# Create your models here.
