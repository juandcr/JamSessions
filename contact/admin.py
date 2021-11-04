from django.contrib import admin
from .models import Mensaje

# Register your models here.
class MensajesAdmin(admin.ModelAdmin):
    readonly_fields=['created','updated']


admin.site.register(Mensaje,MensajesAdmin)