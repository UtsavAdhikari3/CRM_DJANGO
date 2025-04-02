from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def home(request):
    # Check to see if person is logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Check if the username and password are correct
        user = authenticate(request, username=username, password=password)
        # If the user is correct, log them in
        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in')
            return render(request, 'home.html',{})
        # If the user is not correct, return an error message
        else:
            messages.error(request, 'Invalid username or password')
            return render(request, 'home.html',{})
    return render(request, 'home.html',{})


def logout_user(request):
    pass