from django.db import models

from taggit.managers import TaggableManager

from core.models import User

class Question(models.Model):
	title = models.CharField(
		max_length=300, 
		default='QuestionTitle',
		help_text='A memorable identifier for the question')
	content = models.TextField(max_length=500)
	tags = TaggableManager()
	responses = models.IntegerField(default=0)
	yeas = models.IntegerField(default=0)
	nays = models.IntegerField(default=0)
	
	def __str__(self):
		return self.title
	
class Response(models.Model):
	question = models.ForeignKey(Question)
	user = models.ForeignKey(User)
	accepted = models.BooleanField(default=False)
	correction = models.TextField(max_length=500, default='')
