from django.db import models

# Create your models here.
class volunteer(models.Model):
	name=models.CharField(max_length=200)
#	address=models.CharField(max_length=200)
	contact_number=models.CharField(max_length=200)
	email=models.EmailField()
	def __str__(self):
		return self.name
