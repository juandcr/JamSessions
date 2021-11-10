from django.shortcuts import render,HttpResponse
from .models import Testimonio,RedSocial,Texto
# Create your views here.


def home (request):
    testimonios= Testimonio.objects.all() 
    context={
        'testimonios':testimonios,
        'encabezado1':'',
        'encabezado2':'',
        'texto1':'',
        
    }
    return render(request,'core/home.html', context)


def about (request):        
    somos= Texto.objects.filter(name="JamSomos").first()
    return render(request,'core/about.html',{'somos':somos})

def services (request):
    lockoutBasica=Texto.objects.filter(name="lockoutBasica").first()
    lockoutPlus=Texto.objects.filter(name="lockoutPlus").first()
    ep=Texto.objects.filter(name="EP").first()
    lp=Texto.objects.filter(name="LP").first()
    sesionEstudio=Texto.objects.filter(name="sesionEstudio").first()
    liveSessions=Texto.objects.filter(name="liveSession").first()
    porCancion=Texto.objects.filter(name="porCancionBasico").first()
    porCancionPlus=Texto.objects.filter(name="porCancionPlus").first()
    mezclaMasterizacion=Texto.objects.filter(name="mezclaMasterizacion").first()
    podcast=Texto.objects.filter(name="podcast").first()
    podcastVideo=Texto.objects.filter(name="podcastVideo").first()
    
    context={
        'lockoutBasica':lockoutBasica,
        'lockoutPlus':lockoutPlus,
        'ep':ep,
        'lp':lp,
        'sesionEstudio':sesionEstudio,
        'liveSessions':liveSessions,
        'porCancion':porCancion,
        'porCancionPlus':porCancionPlus,
        'mezclaMasterizacion':mezclaMasterizacion,
        'podcast':podcast,
        'podcastVideo':podcastVideo,
    }


    return render(request,'core/services.html',context)