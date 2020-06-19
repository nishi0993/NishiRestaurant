from django.db import models


Choices = [
    ('Mr.', 'MR.'),
    ('Ms.', 'MS.'),
    ('Mrs.', 'MRS.'),
]

class Author(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255, choices=Choices)
    date = models.DateField(blank=True, null=True)
    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=255)
    authors = models.ManyToManyField(Author)
    def __str__(self):
        return self.name



# Create your models here.
