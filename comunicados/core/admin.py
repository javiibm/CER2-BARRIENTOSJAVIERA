from django.contrib import admin
from core.models import Comunicado
from core.models import Categoria

# Register your models here.
class ComunicadoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Comunicado, ComunicadoAdmin)
admin.site.register(Categoria, ComunicadoAdmin)