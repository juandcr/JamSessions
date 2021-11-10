from .models import RedSocial,Texto

def ctx_dict(request):    
    redes=RedSocial.objects.filter(active=True)
    numero=Texto.objects.filter(name="teléfono").first()
    correo=Texto.objects.filter(name="correo").first()
    celular= Texto.objects.filter(name="celular").first()
    direccion= Texto.objects.filter(name="dirección").first()
    footer= Texto.objects.filter(name="footer").first()
    ctx={ 
        'redes': redes,
        'numero': numero,
        'correo':correo,
        'celular':celular,
        'direccion':direccion,
        'footer':footer,
    }
    return ctx