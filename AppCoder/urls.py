from django.urls import path
from AppCoder.views import crear_curso, inicio, cursos, cursos_formulario

urlpatterns = [
    
    path('crearcurso/<camada>', crear_curso),
    path('', inicio, name = 'inicio'),
    path('cursos', cursos, name = 'cursos'),
    path('cursosFormulario', cursos_formulario, name = 'cursos_formulario'),
]