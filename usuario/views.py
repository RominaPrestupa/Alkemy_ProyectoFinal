from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user:
            login(request, user)
            return redirect (reverse('index'))
        else:
            return render(request, 'usuario/login.html', {'msj':'Usuario o Contraseña incorrectos'})
    return render(request, 'usuario/login.html')


def logout_view(request):
    logout(request)
    return render(request, 'usuario/logout.html')

