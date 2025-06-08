from django.shortcuts import render, HttpResponse, redirect
from . forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    return render(request, 'home.html')

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save
            return redirect('login')
        else:
            return HttpResponse('Invalid Information, GO BACK')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'formX': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['usernameX']
        password = request.POST['passwordX']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse('User Not Found')
    else:
     return render(request, 'login.html')

def logout_view(request):
    return HttpResponse("Logout")

def delete_task(request, id):
    return HttpResponse("delete")
