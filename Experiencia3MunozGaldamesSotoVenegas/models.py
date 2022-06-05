from tabnanny import verbose
from django.db import models


class Usuarios(models.Model):
    username = models.CharField(max_length=30,primary_key=True, verbose_name='Nombre de usuario')
    mail = models.CharField(max_length=60, null=False, blank=False,unique=True, verbose_name='Correo')
    password = models.CharField(max_length=60, null=False, blank=False, verbose_name='Contraseña')
    class Meta:
        verbose_name_plural = 'Usuarios'
    def __str__(self):
        return self.username
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        del self
## Create your models here.

