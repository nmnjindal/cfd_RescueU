from django.db import models

# Create your models here.
class donor(models.Model):
	name=models.CharField(max_length=200)
	amount=models.CharField(max_length=200)
	def __str__(self):
		return self.name
	