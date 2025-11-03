from django.shortcuts import render
# core/views.py
from django.http import HttpResponse
# Uma 'view' é uma função que recebe um 'request' e retorna uma 'response'

# Create your views here.
def home(request):
# Vamos retornar a resposta HTTP mais simples: um texto HTML
    return HttpResponse("<h1>Olá, Mundo! Esta é minha primeira página Django!</h1>")

def segunda(request):
    return HttpResponse("<h1>Olá! Essa é a segunda página Django!</h1>")

def login(request):
    return HttpResponse("<input>Entrada!</input>")