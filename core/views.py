from django.shortcuts import render, redirect
from core.models import Evento
# Exige que o usuário esteja logado para acessar a agenda.(1)
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

# redirect
# def index(request):
#    return redirect('/agenda/')

def login_user(request):   #(2)
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "Usuário ou senha inválido")

    return redirect('/')

@login_required(login_url='/login/')
def lista_eventos(request):
    usuario = request.user  # (1)
    evento = Evento.objects.filter(usuario=usuario)  # filtro por usuário (1)
    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados)
