from django.db import models
from django.contrib.auth.models import User

# Create your models here.
NIVEL_CHOICES= [
    ("GEN", "General"), 
    ("PRE", "Ciclo Preescolar"), 
    ("BAS", "Ciclo Básico"), 
    ("MED", "Ciclo Medio")
]

class Categoria(models.Model):
    nombre = models.TextField(max_length=40)
    descripcion = models.TextField(max_length=40)
    def __str__(self):
        return self.nombre

class Comunicado(models.Model):
    titulo = models.TextField(max_length=40)
    detalle = models.TextField(max_length=40)
    nivel = models.CharField(max_length=20, choices= NIVEL_CHOICES)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fecha_envio = models.DateTimeField()
    fecha_ultima_modificacion = models.DateTimeField()
    publicado_por = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.titulo