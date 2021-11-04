from django.db import models

# Create your models here.


class Gallery(models.Model):
    title= models.CharField(verbose_name="Título", max_length=300)
    description= models.TextField(verbose_name="Descripción",blank=True,null=True)
    image= models.ImageField(upload_to='images',null=False, blank=False)
    active= models.BooleanField(default=True,verbose_name="activo")
    created= models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated= models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name="Imagen"
        verbose_name_plural="Imágenes"
        ordering= ['-created']
    
    def __str__(self):
        return self.title