from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.

def signup(request):
    if request.method == "POST":
        firstPassword = request.POST['password']
        secondPassword = request.POST['passwordConfirm']
        if firstPassword == secondPassword:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error': 'Sorry! That username is already in use. Try something cooler!'})
            except User.DoesNotExist:
                userCreated = User.objects.create_user(request.POST['username'], password=request.POST['password'])
                login(request, userCreated)
                return render(request, 'accounts/signup.html')
        else:
            return render(request, 'accounts/signup.html', {'error': 'Passwords don\'t match. Please try again'})
    else:
        return render(request, 'accounts/signup.html')