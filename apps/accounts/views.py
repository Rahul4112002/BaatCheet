from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
def home(request):
    users = User.objects.all()
    return render(request, 'accounts/accounts.html',{'users': users})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
    return render(request,'accounts/login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        User.objects.create_user(
            username=username, 
            password=password
        )
        return redirect('home')
    return render(request,'accounts/register.html')

def user_logout(request):
    logout(request)
    return redirect('home')

def searched(request):
    query = request.GET.get('query')
    users = User.objects.filter(username__icontains = query)
    return render(request, 'accounts/accounts.html',{'users': users})

