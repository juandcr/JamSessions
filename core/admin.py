from django.contrib import admin
from .models import Testimonio,RedSocial,Texto
# Register your models here.


class TestimonioAdmin(admin.ModelAdmin):
    readonly_fields=['created','updated']

class RedSocialAdmin(admin.ModelAdmin):
    readonly_fields=['created','updated']

class TextoAdmin(admin.ModelAdmin):
    readonly_fields=['created','updated']



admin.site.register(Testimonio,TestimonioAdmin)
admin.site.register(RedSocial,RedSocialAdmin)
admin.site.register(Texto,TextoAdmin)



