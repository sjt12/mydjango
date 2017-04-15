from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

class UserManager(BaseUserManager):
	use_in_migrations = True
	
	def _create_user(self, username, password, **extra_fields):
		"""
		Creates and saves a User with given username
		"""
		if not username:
			raise ValueError('The given username must be set')
		
		user = self.model(username=username, **extra_fields)
		user.set_password(password)
		user.save(using=self.db)
		return user
		
	def create_user(self, username, **extra_fields):
		extra_fields.setdefault('is_superuser', False)
		return self._create_user(username, email_me, "password", **extra_fields)
		
	def create_superuser(self, username, password, **extra_fields):
		extra_fields.setdefault('is_superuser', True)
		extra_fields.setdefault('is_staff', True)
		
		if extra_fields.get('is_superuser') is not True:
			raise ValueError('Superuser must have is_superuser = True')
			
		return self._create_user(username, password, **extra_fields)
		
		
