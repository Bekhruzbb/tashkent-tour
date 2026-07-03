from django.shortcuts import render, redirect, HttpResponse
from .forms import LoginForm, RegisterForm
from django.contrib.auth import login, logout
# Create your views here.


def show_login_page(request):
    login_form = LoginForm()
    context = {
        'login_form': login_form

    }
    return render(request, 'users/login.html', context)


def show_registration_page(request):
    register_form = RegisterForm()
    context = {
        'register_form': register_form
    }
    return render(request, "users/registration.html", context)


def login_user(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user:
                login(request, user)
                return redirect('main:home')
    else:
        form = LoginForm()
        return HttpResponse(form.errors)

    return render(request, "main/main.html", {
        "login_form": form
    })


def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(data=request.POST, files=request.FILES)

        if form.is_valid():
            form.save()
            return redirect('users:login')

        else:
            form = RegisterForm()
            print(form.errors)

        return render(request, "users/login.html", {
            "register_form": form
        })


def logout_user(request):
    logout(request)
    return redirect("main:home")