from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Courses(models.Model):
	class_id=models.IntegerField(default=0)
	class_name=models.CharField(max_length=50)
	class_description=models.CharField(max_length=500)

	def __str__(self):
		return self.title