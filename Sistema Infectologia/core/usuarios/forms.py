from django import forms
from django.forms import ModelForm
from core.usuarios.models import Usuario

class UserForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Usuario
        fields = ('first_name', 'last_name','cedula', 'email', 'username', 'password', 'is_active', 'sexo')
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese sus nombres',
                    'class': 'input-style form-control',
                    'autofocus': True
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese sus apellidos',                    
                    'class': 'input-style form-control',
                }
            ),
            'cedula': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese su cédula',                    
                    'class': 'input-style form-control',
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Correo Electronico ...',                    
                    'class': 'input-style form-control',
                }
            ),
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese su nombre de usuario',
                    'autocomplete': 'off',
                    'class': 'input-style form-control'
                }
            ),
            'password': forms.PasswordInput(render_value=True,
                attrs={
                    'placeholder': 'Ingrese su contraseña',
                    'class': 'input-style form-control',
                }
            ),
            'sexo': forms.Select(attrs={
                'class': 'select2, form-control',
                'style': 'width: 100%'
            }),
        }
        exclude = ['last_login', 'date_joined', 'is_superuser', 'is_staff', 'is_active', 'user_permissions', 'groups']

    # Para guardar el formulario
    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                #Obtener contraseña ingresada
                pwd = self.cleaned_data['password']
                u = form.save(commit=False)
                # Se verifica que el usuario sea nuevo para encriptar contraseña
                if u.pk is None:
                    u.set_password(pwd)
                else:
                    #Se consulta el usuario que se esta editando y se verifica si la contraseña es diferente para encriptarla
                    user = Usuario.objects.get(pk=u.pk)
                    if user.password != pwd:
                        u.set_password(pwd)
                u.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

