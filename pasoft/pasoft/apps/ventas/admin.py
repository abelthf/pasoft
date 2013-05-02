#que tiene el admin de django
from django.contrib import admin
from pasoft.apps.ventas.models import cliente,producto

#para registrarlo en el admin
admin.site.register(cliente)
admin.site.register(producto)