from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request, name):
    mensagem = f"Olá, {name}! Seja bem vindo ao nosso site com Django!"
    return HttpResponse(mensagem)

# Create your views here.
def bye(request, name):
    mensagem = f"Olá, {name}! Volte sempre!!"
    return HttpResponse(mensagem)