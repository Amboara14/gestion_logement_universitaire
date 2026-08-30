from django.shortcuts import render

def login_view(request):
    return render(request, "athentification/login.html")

def register_view(request):
    return render(request, "athentification/register.html")
