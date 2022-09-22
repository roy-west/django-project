from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


def login_view(request):
    context = {}
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username, '\n', password)
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is None:
            context = {"error": "Something wrong ! Username or password is not correct !"}
        else:
            login(request, user)
            return redirect('/admin')
    return render(request, "accounts/login.html", context)
