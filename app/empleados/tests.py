
import sys
sys.path.append('D:/Documentos/Curso desarrollo web/python/curso_django/curso 1/app/')

from config.wsgi import *
from empleados.models import Type
# from django.test import TestCase

# Create your tests here.

# insercion 
t = Type()
t.name = 'accionista'
t.save()

# listar
query = Type.objects.all()
print(query)

# edicion 

t = Type.objects.get(id=1)
t.name = 'cambio'
t.save()
print(t.name)

# eliminacion

t = Type.objects.get(id=1)
t.delete()

