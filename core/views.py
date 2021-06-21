from django.shortcuts import render,HttpResponse
from .models import Testimonio,RedSocial,Texto
# Create your views here.


def home (request):
    """testimonios= Testimonio.objects.all()
    encabezado1= Texto.objects.get(name="Encabezado1")
    texto1= Texto.objects.get(name="Texto1")
    encabezado2= Texto.objects.get(name="Encabezado2")
    """

    context={
        'testimonios':'',
        'encabezado1':'',
        'encabezado2':'',
        'texto1':'',
        
    }
    return render(request,'core/home.html', context)


def about (request):    
    return render(request,'core/about.html')