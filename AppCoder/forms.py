# from django.forms import Form, CharField, IntegerField
from django import forms

class CursoForm(forms.Form):
    curso = CharField() 
    camada = IntegerField()   