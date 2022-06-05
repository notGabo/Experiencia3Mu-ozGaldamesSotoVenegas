from django.http import HttpResponseRedirect,JsonResponse
from django.shortcuts import render  
from django.forms.models import model_to_dict
from .models import Usuarios

def index(request):
    context = {} 
    context['esta_logueado'] = False
    if request.method == 'GET':
        if 'user' in request.session:
            context['esta_logueado'] = True
        return render(request, 'Experiencia3MunozGaldamesSotoVenegas/index.html', context)
    elif request.method == 'POST':
        if 'user' in request.session:
            context['esta_logueado'] = True
        data = dict(request.POST)
        if 'registrar-btn' in data:
            username = data['usernameRegistro'][0]
            email = data['emailRegistro'][0]
            password = data['passwordRegistro'][0]
            user = Usuarios(username,email,password)
            user.save()
            print(username, email, password)
        elif 'login-btn' in data:
            username = data['username'][0]
            password = data['password'][0]
            if Usuarios.objects.filter(username = username, password = password).exists():
                with Usuarios.objects.get(username = username) as user:
                    request.session['user'] = model_to_dict(user)
                print('login correcto')
            else:
                print('login incorrecto')
            print('logueando')
        else:
            print('error')            
        return render(request, 'Experiencia3MunozGaldamesSotoVenegas/index.html',context)

def logout(request):
    request.session.flush()
    response = JsonResponse({'success': 'Sesion cerrada'})
    response.status_code = 200
    return response

def contactanos(request):
    print(request.session['user'])
    return render(request, 'Experiencia3MunozGaldamesSotoVenegas/contactanos.html')

def exteriores(request):
    return render(request, 'Experiencia3MunozGaldamesSotoVenegas/PlantasExteriores.html')

def interiores(request):
    return render(request, 'Experiencia3MunozGaldamesSotoVenegas/PlantasInteriores.html')

def arboles(request):
    return render(request, 'Experiencia3MunozGaldamesSotoVenegas/TiposDeArboles.html')

def quienesSomos(request):
    return render(request, 'Experiencia3MunozGaldamesSotoVenegas/quienesSomos.html')

def registrarSolicitud(request):
    return render(request, 'Experiencia3MunozGaldamesSotoVenegas/registrarSolicitud.html')

def tyc(request):
    return render(request, 'Experiencia3MunozGaldamesSotoVenegas/terminosycondiciones.html')

def inicioSesion(request):
    return render(request, 'Experiencia3MunozGaldamesSotoVenegas/inicioSesion.html')
# Create your views here.
