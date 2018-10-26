from django.shortcuts import render
from .forms import SignUpForm
from django.core.mail import send_mail
from django.conf import settings
from volunteers.models import volunteer
import geocoder
from django.contrib.auth.decorators import login_required
# Create your views here.

def signup(request):
    if(request.method=='POST'):
        form=SignUpForm(request.POST)
        if(form.is_valid()):
            form.save()
    else:
        form=SignUpForm()
    return render(request,'users/signup.html',{'form' : form})

@login_required
def sos(request):
	subject='Help is needed at this location'
	g=geocoder.ip('me')
	message='Rescue as fast as possible\n'+'http://www.google.com/maps/place/'+str(g.latlng[0])+','+str(g.latlng[1])
	email_from = settings.EMAIL_HOST_USER
	recipient_list=[]
	list=volunteer.objects.all()
	#for entry in list:
	#	recipient_list.append(entry.email)
	recipient_list.append('naman@iitk.ac.in')
	send_mail(subject,message,email_from,recipient_list)
	return render(request,'users/sos.html')


