from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth


# Create your views here.

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('signin')
    else:
        return render(request, 'signin.html')


def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email,
                                                first_name=first_name, last_name=last_name)
                user.save()
                return redirect('signin')
        else:
            messages.info(request, 'Password not matching')
            return redirect('signup')

    else:
        return render(request, 'signup.html')


def terms(request):
    return render(request, 'terms.html')


def signout(request):
    auth.logout(request)
    return redirect('/')



