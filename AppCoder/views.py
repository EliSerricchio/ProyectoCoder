from django.shortcuts import render,redirect
from django.http import HttpResponse
from AppCoder.models import Curso
from AppCoder.forms import CursoFormulario

def crear_curso(request, camada):
    curso = Curso (nombre = 'Python', camada = camada)
    curso.save()
    return HttpResponse(f'Curso Creado! {camada}')  

def inicio (request):
    return render(request, 'AppCoder/inicio.html') 
    

def cursos (request):
    return render(request, 'AppCoder/cursos.html', 
                  {'cursos': Curso.objects.all()})  

def profesores (request):
    return HttpResponse('Profesores')

def estudiantes (request):
    return HttpResponse('Estudiantes')

def entregables (request):
    return HttpResponse('Entregables')

def cursos_formulario (request): #se usan las mismas variables que en el forms 
    if request.method == 'POST':
        formulario = CursoForm(request.POST)
        # curso = request.POST ['curso']
        # camada = request.POST ['camada']
        if formulario.is_valid():
            data = formulario.cleaned_data
            Curso.objects.create(nombre=data['curso'], camada=data['camada']) #curso = curso de forms.py
            return redirect('cursos')
    else:
        formulario = CursoForm()
    return render(request, 'AppCoder/cursosFormulario.html', {'formulario': formulario}) 