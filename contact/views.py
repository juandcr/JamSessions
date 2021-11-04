from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import ContactForm
from .models import Mensaje

# Create your views here.
def contacto(request):
    contact_form=ContactForm()    
    if(request.method=="POST"):
        contact_form=ContactForm(data=request.POST)    
        if (contact_form.is_valid):
            name= request.POST.get('name','')
            phone= request.POST.get('phone','')
            email= request.POST.get('email','')
            content= request.POST.get('content','')
            #Creation of a new object using form data
            mensaje= Mensaje(name=name, phone= phone,email=email,text=content)
            mensaje.save()
            #ok
            return redirect(reverse('contact')+'?ok')

    return render(request,'contact/contacto.html',{'form': contact_form})