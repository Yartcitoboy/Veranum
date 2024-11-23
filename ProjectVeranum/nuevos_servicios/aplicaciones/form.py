from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'

class LoginForm(forms.Form):
    rut = forms.CharField(max_length=12, label="RUT", widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Ingrese su RUT'
    }))
    password = forms.CharField(max_length=128, label="Contraseña", widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'Ingrese su contraseña'
    }))