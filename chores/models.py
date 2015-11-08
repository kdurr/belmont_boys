from django.db import models

class Roomie(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Chore(models.Model):
    description = models.CharField(max_length=200)
    events = models.ManyToManyField('Roomie', through='Event')

    def __str__(self):              # __unicode__ on Python 2
        return self.description

class Event(models.Model):
    roomie = models.ForeignKey('Roomie')
    chore = models.ForeignKey('Chore')
    date = models.DateTimeField(auto_now=True)
    comment = models.CharField(max_length=200)
