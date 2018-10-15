from django.forms import ModelForm
from .models import donor

class PostForm(ModelForm):
	class Meta:
		model=donor
		fields={'name','amount'}
