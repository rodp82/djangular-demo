# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse


# Create your models here.
class Actor(models.Model):
    name = models.CharField(max_length=30)

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.
        Also used by django admin to add a 'view on site' link
        """
        return reverse('actor_detail', args=[str(self.id)])

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=30)
    year = models.IntegerField()
    actors = models.ManyToManyField(Actor, through='Cast')

    def __str__(self):
        return '{} ({})'.format(self.title, self.year)

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.
        Also used by django admin to add a 'view on site' link
        """
        return reverse('movie_detail', args=[str(self.id)])


class Cast(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    salary = models.IntegerField()

    def __str__(self):
        return '{} - {}'.format(self.movie, self.actor)