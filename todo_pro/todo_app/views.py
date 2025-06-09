from django.shortcuts import render, HttpResponse, redirect
from . forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Task

@login_required
def home(request):
    data = Task.objects.all()
    return render(request, 'home.html', {'data':data})

def add(request):
    if request.method == 'POST':
        tododata = request.POST['add']
        Task.objects.create(title=tododata)
        return redirect('home')
    else: 
        return render(request, 'home.html')

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return HttpResponse('Invalid Information, GO BACK')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'formX': form})


def login_view(request):
    if request.method == 'POST':
        usernameY = request.POST['usernameX']
        passwordY = request.POST['passwordX']
        user = authenticate(request, username=usernameY, password=passwordY) 
        if user:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse('User Not Found')
    else:
     return render(request, 'login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

def delete_task(request, id):
    return HttpResponse("delete")
