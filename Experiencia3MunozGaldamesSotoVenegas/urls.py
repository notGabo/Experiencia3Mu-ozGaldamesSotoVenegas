
from django.urls import path 
from .views import index, contactanos, exteriores, interiores, arboles, quienesSomos, registrarSolicitud, tyc, logout


urlpatterns = [
    path('', index, name='index'),
    path('index.html', index, name='index'),
    path('contactanos.html', contactanos, name='Contactanos'),
    path('PlantasExteriores.html', exteriores, name='Exteriores'),
    path('PlantasInteriores.html', interiores, name='Interiores'),
    path('TiposDeArboles.html', arboles, name='Arboles'),
    path('quienesSomos.html', quienesSomos, name='Quienes Somos'),
    path('registrarSolicitud.html', registrarSolicitud, name='Registrar Solicitud'),
    path('terminosycondiciones.html', tyc, name='Terminos y condiciones'),
    path('api/v1/logout',logout,name='logout')
]