from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import  LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.forms import UserCreationForm

def home_page(request):
    if request.session.has_key('username'):
        username = request.session['username']
        return render(request, 'home_page.html')
    return render(request, "home_page.html")

def index(request):
    if request.session.has_key('username'):
        username = request.session['username']
        return render(request, 'home_page.html')

    return render(request, "registration/index.html")

def log_out(request):
    try:
        del request.session['username']
    except:
        pass
    form = LoginForm(request.POST or None)
    return render(request, 'login.html')
def login_page(request):
    form = LoginForm(request.POST or None)
    # print(request.user.is_authenticated)
    context = {
        "form": form
    }
    # print(request.user.is_authenticated())
    # print("User logged in")
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            request.session['username'] = username
            if user is not None:
                login(request, user)
                # context['form'] = LoginForm()
                return redirect("home")
            else:
                print("error")

    return render(request, "registration/login.html", context)

user = get_user_model()
def register_page(request):
    if request.session.has_key('username'):
        username = request.session['username']
        return render(request, 'home_page.html')

    form = RegisterForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = user.objects.create_user(username, password, email)
        print(new_user)
        # messages.success(request, 'Form submission successful')
        return redirect('login')

    return render(request, "registration/registration.html", context)

