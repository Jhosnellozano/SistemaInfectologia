from django import forms
from django.contrib.auth import authenticate
from core.usuarios.models import Usuario


class AuthenticationForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'style': 'font-size: 13px;',
        'required': True,
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'style': 'font-size: 13px;',        
        'name': 'password',
        'required': True,
    }))

    def clean(self):
        cleaned = super().clean()
        username = cleaned.get('username', '')
        password = cleaned.get('password', '')
        if len(username) == 0:
            raise forms.ValidationError('Ingrese su nombre de usuario')
        elif len(password) == 0:
            raise forms.ValidationError('Ingrese su contraseña')

        queryset = Usuario.objects.filter(username=username)
        if queryset.exists():
            user = queryset[0]
            if not user.is_active:
                raise forms.ValidationError('El usuario ha sido bloqueado. Comuníquese con el administrador.')
            if authenticate(username=username, password=password) is None:
                raise forms.ValidationError(f"La contraseña ingresada es incorrecta, por favor intentelo de nuevo.")
            return cleaned
        raise forms.ValidationError('Por favor introduzca el nombre de usuario y la clave correctos para una cuenta de personal. Observe que ambos campos pueden ser sensibles a mayúsculas.')

    def get_user(self):
        username = self.cleaned_data.get('username')
        return Usuario.objects.get(username=username)