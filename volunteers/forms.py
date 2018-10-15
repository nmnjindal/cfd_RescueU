from django.forms import ModelForm
from .models import volunteer

class PostForm(ModelForm):
	class Meta:
		model= volunteer
		fields=('name','contact_number','email')
		