from django.db import models
from django.utils import timezone
class User(models.Model):
	first_name = models.CharField(max_length=50, blank=False)
	last_name = models.CharField(max_length=50, blank=False)
	email = models.CharField(max_length=50, blank=False)
	password = models.CharField(max_length=50, blank=False)
	description = models.TextField(default='',blank=True)
	admin = models.BooleanField(default=False)
	created_at = models.DateTimeField(default=timezone.now)
	updated_at = models.DateTimeField(default=timezone.now)
	class Meta:
		db_table = 'users'

class Message(models.Model):
	message = models.TextField(blank=False)
	recepient = models.ForeignKey(User, related_name='recepient', blank=False)
	sender = models.ForeignKey(User, related_name='sender', blank=False)
	created_at = models.DateTimeField(default=timezone.now)
	updated_at = models.DateTimeField(default=timezone.now)
	class Meta(object):
		db_table = 'messages'

class Comment(models.Model):
	comment = models.TextField(blank=False)
	message = models.ForeignKey(Message,blank=False)
	user = models.ForeignKey(User,blank=False)
	created_at = models.DateTimeField(default=timezone.now)
	updated_at = models.DateTimeField(default=timezone.now)	
	class Meta(object):
		db_table = 'comments'
		