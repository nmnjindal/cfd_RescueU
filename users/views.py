from django.shortcuts import render
from .forms import SignUpForm
# Create your views here.

def signup(request):
    if(request.method=='POST'):
        form=SignUpForm(request.POST)
        if(form.is_valid()):
            form.save()
    else:
        form=SignUpForm()
    return render(request,'users/signup.html',{'form' : form})