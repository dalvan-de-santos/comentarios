from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import comentario
from django.contrib.auth import logout


def create_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username)
        if user.exists():
            return HttpResponse('Usuário já existe.')
        user = User.objects.create_user(username=username, password=password)
        user.save()
        login(request, user)
        return redirect('comentarios')
    return render(request, 'create_user.html')


@login_required
def comentarios(request):
    if request.method == 'POST':
        texto = request.POST.get('texto')
        novo_comentario = comentario(user=request.user, texto=texto)
        novo_comentario.save()
        return redirect('comentarios')
    comentarios = comentario.objects.all().order_by('-data_criacao')
    return render(request, 'comentarios.html', {'comentarios': comentarios})


def logout_view(request):
    logout(request)
    return redirect('create_user')
