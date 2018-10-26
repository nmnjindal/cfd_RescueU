from django.shortcuts import render
from .forms import SignUpForm
from django.core.mail import send_mail
from django.conf import settings
from volunteers.models import volunteer
import geocoder
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .forms import commentform
# Create your views here.

def home(request):
	return render(request,'users/home.html')

def signup(request):
    if(request.method=='POST'):
        form=SignUpForm(request.POST)
        if(form.is_valid()):
            form.save()
            return HttpResponseRedirect('http://127.0.0.1:8000/')
    else:
        form=SignUpForm()
    return render(request,'users/signup.html',{'form' : form})

def hospitals(request):
	return render(request,'users/hospitals.html')

@login_required
def sos(request):
	if(request.method=='POST'):
		comment=commentform(request.POST)
		if(comment.is_valid()):
			subject='Help is needed at this location'
			g=geocoder.ip('me')
			message='Rescue as fast as possible\n'+'http://www.google.com/maps/place/'+str(g.latlng[0])+','+str(g.latlng[1])+'\n'+comment.cleaned_data['comment']
			email_from = settings.EMAIL_HOST_USER
			recipient_list=[]
			list=volunteer.objects.all()
			for entry in list:
				recipient_list.append(entry.email)
			send_mail(subject,message,email_from,recipient_list)
			return render(request,'users/sos_sent.html')
	else:
		form=commentform()
		return render(request,'users/comment.html',{'form':form})





