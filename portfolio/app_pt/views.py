from django.shortcuts import render
from django.views import View

def pagina_inicial(request):
    return render(request,'pagina_inicial.html')
