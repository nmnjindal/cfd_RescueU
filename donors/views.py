from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import donor
from .forms import PostForm
def index(request):
	list=donor.objects.order_by('-amount')
	context={'list': list}
	return render(request,'donors/index.html',context)

def donate(request):
	if(request.method=='POST'):
		form=PostForm(request.POST)
		if(form.is_valid()):
			form.save()
			return HttpResponseRedirect('http://127.0.0.1:8000/donors/')
	else:
		form=PostForm()
	return render(request,'donors/donate.html',{'form' : form})
