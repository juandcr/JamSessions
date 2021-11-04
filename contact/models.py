from django.db import models

# Create your models here.
class Mensaje(models.Model):
    name= models.CharField(verbose_name="Nombre", null=False, blank=False, max_length=100,default="Fix")
    email= models.EmailField(verbose_name="Correo",null=False,blank=False)
    phone= models.TextField(verbose_name="Teléfono", null=False, blank=False,max_length=10,default="555555")
    text= models.TextField(verbose_name="Descripción", null=False, blank=False)
    active=models.BooleanField(verbose_name="activo",default=True)
    created= models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated= models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")
    
    class Meta:
        verbose_name="Mensaje"
        verbose_name_plural="Mensajes Contact Point"
        ordering= ['-created']
    
    def __str__(self):
        return self.email