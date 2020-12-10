from django.contrib import admin
from .models import Ilustracion
from .models import Imagenes
from .models import Editor
# Register your models here.
admin.site.register(Ilustracion)
admin.site.register(Imagenes)
admin.site.register(Editor)