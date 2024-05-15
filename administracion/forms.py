from django import forms
from .models import *

from django import forms
from django.contrib.auth.forms import UserCreationForm
from administracion.models import MyUser

class LoginForm(forms.Form):
    email = forms.EmailField(label="Correo electrónico")
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)

class MyUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = MyUser
        fields = ('email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
class CabezaForm(forms.ModelForm):
    class Meta:
        model = Cabeza
        fields = "__all__"  # Esto incluirá todos los campos del modelo Cabeza en el formulario

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock  # Especifica el modelo al que está vinculado el formulario
        fields = "__all__"  # Especifica los campos que deseas incluir en el formulario