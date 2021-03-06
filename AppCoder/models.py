# from django.db import models
from django.db.models import Model 
from django.db.models.fields import BooleanField, CharField, DateField, EmailField, IntegerField  


class Curso(Model):
    nombre = CharField(max_length=40, verbose_name = 'Descripcion del curso')
    camada = IntegerField()
    def __str__ (self):
        return f'Curso {self.nombre} ({self.camada})'
    
class Estudiante(Model):
    nombre= CharField(max_length=30)
    apellido= CharField(max_length=30)
    email= EmailField()

class Profesor(Model):
    nombre= CharField(max_length=30)
    apellido= CharField(max_length=30)
    email= EmailField()
    profesion= CharField(max_length=30)

class Entregable(Model):
    nombre= CharField(max_length=30)
    fechaDeEntrega = DateField()  
    entregado = BooleanField()    

