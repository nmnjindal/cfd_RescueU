from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from .forms import PostForm
from django.http import HttpResponseRedirect
from .models import volunteer
from django.core.exceptions import ValidationError


# Create your views here.

def index(request):
    return render(request, 'volunteers/index.html')

def register (request):
	if request.method == 'POST':
		form=PostForm(request.POST)
		if(form.is_valid()):		
			form.save()
			return HttpResponseRedirect('http://127.0.0.1:8000/volunteer/list/')
	else:
		form=PostForm()
	return render(request, 'volunteers/register.html',{ 'form' : form })

def list(request):
	vol_list=volunteer.objects.order_by('-name')
	context={'vol_list':vol_list}
	return render(request, 'volunteers/list.html', context)