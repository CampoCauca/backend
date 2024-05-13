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