from django.utils import timezone
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

# CustomUserManager is Required because we are not using Django's built in User class
class CustomUserManager(BaseUserManager):
	def _create_user(self, email, password, is_superuser, is_staff, first_name, last_name):
		now = timezone.now

		if not email:
			raise ValueError('Email is required')

		email = self.normalize_email(email)
		user = self.model(email=email, is_superuser=is_superuser, is_staff=is_staff, first_name=first_name, last_name=last_name)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_user(self, email, first_name, last_name, password=None,):
		return self._create_user(email, password, False, False, first_name, last_name)

	def create_superuser(self, email, password, first_name, last_name):
		return self._create_user(email, password, True, True, first_name, last_name)

class CustomUser(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField(
		verbose_name = 'email address',
		max_length=255,
		unique=True
	)
	first_name = models.CharField(max_length=50, blank=False)
	last_name = models.CharField(max_length=50, blank=False)
	description = models.TextField(default='',blank=True)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False) # designates whether this user can access the admin site
	created_at = models.DateTimeField(default=timezone.now)
	updated_at = models.DateTimeField(default=timezone.now)

	objects = CustomUserManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['first_name','last_name']

	def get_full_name(self):
		return self.first_name + ' ' + self.last_name

	def get_short_name(self):
		return self.first_name

	def __unicode__(self):
		return self.email
	def to_dictionary(self):
		if self.is_superuser:
			return {'first_name': self.first_name, 'last_name': self.last_name, 'email': self.email, 'description': self.description, 'is_superuser': self.is_superuser, 'is_active': self.is_active, 'is_staff': self.is_staff}
		return {'first_name': self.first_name, 'last_name': self.last_name, 'email': self.email, 'description': self.description, 'is_active': self.is_active}

	def is_superuser(self):
		# is this member a staff?
	    return self.is_superuser

class Message(models.Model):
	message = models.TextField(blank=False)
	recepient = models.ForeignKey(CustomUser, related_name='recepient', blank=False)
	sender = models.ForeignKey(CustomUser, related_name='sender', blank=False)
	created_at = models.DateTimeField(default=timezone.now)
	updated_at = models.DateTimeField(default=timezone.now)

	def to_dictionary(self):
		return {'message': self.message, 'recepient': self.recepient, 'sender': self.sender, 'created_at': self.created_at, 'updated_at': self.updated_at}

	def __unicode__(self):
		return self.message

	def get_id(self):
		return self.id

	class Meta(object):
		db_table = 'messages'

class Comment(models.Model):
	comment = models.TextField(blank=False)
	message = models.ForeignKey(Message,blank=False)
	user = models.ForeignKey(CustomUser,blank=False)
	created_at = models.DateTimeField(default=timezone.now)
	updated_at = models.DateTimeField(default=timezone.now)	
	class Meta(object):
		db_table = 'comments'
		