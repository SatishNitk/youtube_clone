from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone
# Create your models here.

class Video(models.Model):
	user = models.ForeignKey(User, on_delete= models.CASCADE)
	title = models.CharField(max_length=50)
	description= models.TextField(max_length=300)
	# path = models.CharField(max_length=50)
	video_file = models.FileField(upload_to='video/')
	datetime = models.DateTimeField(default=timezone.now(), blank=True)

	def __str__(self):
		return self.title

class Comment(models.Model):
	text = models.TextField(max_length=300)
	datetime = models.DateTimeField(default=timezone.now(),blank=True)
	user = models.ForeignKey(User, on_delete= models.CASCADE)
	video = models.ForeignKey(Video, on_delete= models.CASCADE)



