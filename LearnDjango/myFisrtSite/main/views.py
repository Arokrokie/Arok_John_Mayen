from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, "home.html")


# login views
def login(request):
    return render(request, "login.html")


# signup views
def signup(request):
    return render(request, "signup.html")
