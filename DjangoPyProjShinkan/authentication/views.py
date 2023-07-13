from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from .forms import UploadDataForm
# Create your views here.

def welcome(request):
    return render(request, 'authentication/welcome.html')
@csrf_exempt
def loginview(request):
    if request.method == 'POST':
        
        username = request.POST['username']
        passwor = request.POST['passwor']
        user = authenticate(request, username=username, password=passwor)
        if user is not None:
            login(request, user)
            return render(request, 'authentication/uploaddata.html')  # Redirect to the uploaddata page
        else:
            message = 'Authentication failed. Please try again.'  # Error message for authentication failure
            return render(request, 'authentication/loginview.html', {'message': message})
    else:
        return render(request, 'authentication/loginview.html')
    

def uploaddata(request):
    return render(request, "authentication/uploaddata.html")

