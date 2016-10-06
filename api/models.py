from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Users(models.Model):
	user = models.CharField(max_length=200, unique=True)
	created = models.DateTimeField(auto_now=True)
	username = models.CharField(max_length=100, blank=True)

class Polls(models.Model):
	poll = models.CharField(max_length=200)
	user = models.ForeignKey(Users, on_delete=models.DO_NOTHING)
	question = models.CharField(max_length=500)
	loc_lat = models.DecimalField(max_digits=9, decimal_places=6)
	loc_lng = models.DecimalField(max_digits=9, decimal_places=6)
	created = models.DateTimeField(auto_now=True)

class PollOptions(models.Model):
	poll = models.ForeignKey(Polls, on_delete=models.DO_NOTHING)
	option = models.CharField(max_length=200)

class Votes(models.Model):
	poll = models.ForeignKey(Polls, on_delete=models.DO_NOTHING)
	user = models.ForeignKey(Users, on_delete=models.DO_NOTHING)
	vote = models.ForeignKey(PollOptions, on_delete=models.DO_NOTHING)
	created = models.DateTimeField(auto_now=True)