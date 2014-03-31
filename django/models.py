from django.db import models
from django import forms

# Create your models here.

class ACCESS:
    PUBLIC = 1
    PRIVATE = 2

ACCESS_CHOICES = ((ACCESS.PUBLIC,'Public'),(ACCESS.PRIVATE,'Private'))


class Poll(models.Model):
	question = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	access = models.IntegerField(choices=ACCESS_CHOICES)

class Choice(models.Model):
	poll = models.ForeignKey(Poll)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

class Publication(models.Model):
	title = models.CharField(max_length=30)

	def __unicode__(self):
		return self.title

	class Meta:
		ordering = ('title',)

class Article(models.Model):
	headline = models.CharField(max_length=100)
	publications = models.ManyToManyField(Publication)

	def __unicode__(self):
		return self.headline

	class Meta:
		ordering = ('headline',)

