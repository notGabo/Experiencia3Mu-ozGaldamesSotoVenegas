
from django import forms
from django.forms import ModelForm
from .models import Usuarios


#class LoginForm(ModelForm):
#    class Meta:
#        model = Usuarios
#        fields =  ['username','password']

#class RegisterForm(ModelForm):
#    username = forms.CharField(label='Usuario')
#    email1 = forms.EmailField(label='Correo')
#    email2 = forms.EmailField(label='Confirma correo')
#    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
#    password2 = forms.CharField(label='Confirma contraseña', widget=forms.PasswordInput)
#
#    class Meta:
#        model = Usuarios
#        fields = ['username', 'email1', 'email2', 'password1', 'password2']
#        help_texts = {k:"" for k in fields}


class RegisterForm(ModelForm):
    class Meta:
        model = Usuarios
        fields = ['username', 'email1', 'email2', 'password1', 'password2',]