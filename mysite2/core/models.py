from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser

from .managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):
	SCHOOL = 'SC'
	BACHELOR = 'BA'
	MASTER = 'MA'
	DOCTOR = 'DR'
	EDU_CHOICES = (
		(SCHOOL, 'School'),
		(BACHELOR, 'Bachelors Degree'),
		(MASTER, 'Masters Degree'),
		(DOCTOR, 'Doctorate'),
	)
	
	username = models.CharField(max_length=150, unique=True)
	age = models.IntegerField(default=20)
	education = models.CharField(max_length=2, default=SCHOOL, choices=EDU_CHOICES)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)
	
	objects = UserManager()
	
	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = []
	
	class Meta:
		verbose_name = 'user'
		verbose_name_plural = 'users'
		
	def get_full_name(self):
		return self.username
		
	def get_short_name(self):
		return self.username
	
