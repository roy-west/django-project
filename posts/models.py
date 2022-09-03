from django.db import models


# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    publish = models.DateField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

""""
# one to one relationship
class Country(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# one to many relationship
class Capital(models.Model):
    country = models.OneToOneField(Country,
                                   on_delete=models.CASCADE,
                                   primary_key=True)

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class City(models.Model):
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=250)


class Subject(models.Model):
    teachers = models.ManyToManyField(Teacher)
    title = models.CharField(max_length=250)
"""