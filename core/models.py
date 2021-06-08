from django.db import models

# Create your models here.
class Testimonio(models.Model):
    testigo= models.CharField(max_length=150,verbose_name="Persona")
    text=  models.TextField(verbose_name="Testimonio")
    active= models.BooleanField(verbose_name="activo",default=True)
    created= models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated= models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")
    

    class Meta:
        verbose_name="Testimonio"
        verbose_name_plural="Testimonios"
        ordering= ['-created']
    
    def __str__(self):
        return self.testigo
    

class RedSocial(models.Model):
    name= models.CharField(max_length=30, verbose_name="Red social")
    url=models.CharField(max_length=100,verbose_name="enlace")
    icon= models.CharField(max_length=50, verbose_name="font awesome icon")
    active=models.BooleanField(verbose_name="activo")
    created= models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated= models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")
    
    class Meta:
        verbose_name="Red social"
        verbose_name_plural="Redes sociales"
        ordering= ['-created']
    
    def __str__(self):
        return self.name
    

class Texto(models.Model):
    name= models.CharField(max_length=30, verbose_name="Identificador")
    text=  models.TextField(verbose_name="Texto")
    description=  models.TextField(verbose_name="Descripción del texto")
    created= models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated= models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")
    
    class Meta:
        verbose_name="Texto"
        verbose_name_plural="Textos"
        ordering= ['-created']
    
    def __str__(self):
        return self.name
    



