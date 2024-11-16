from django import forms
from datetime import datetime
from django.forms import ModelForm

from core.hospital.models import Paciente, Doctor, Cita

class PacienteForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['autofocus'] = True

    class Meta:
        model = Paciente
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={
                'placeholder': 'Ingrese el primer y segundo nombre', 
                'class': 'form-control'
            }),
            'apellido': forms.TextInput(attrs={
                'placeholder': 'Ingrese el primer y segundo apellido', 
                'class': 'form-control'
            }),
            'cedula': forms.TextInput(attrs={
                'placeholder': 'Ingrese un número de cedula', 
                'class': 'form-control'
            }),
            'telefono': forms.TextInput(attrs={
                'placeholder': 'Ingrese su número de teléfono', 
                'class': 'form-control'
            }),
            'fecha_nacimiento': forms.DateInput(
                format='%Y-%m-%d', attrs={
                'class': 'form-control border-right-0 datetimepicker-input',
                'id': 'fecha_nacimiento',
                'value': datetime.now().strftime('%Y-%m-%d'),
                'data-target': '#fecha_nacimiento',
                'data-toggle': 'datetimepicker',
            }),
            'direccion': forms.Textarea(attrs={
                'class': 'form-control',
                'required': False,
                'rows': '2',
                'placeholder': 'Ingrese una dirección',
            }),
            'sexo': forms.Select(attrs={
                'class': 'select2, form-control',
                'style': 'width: 100%'
            }),
            'tipo_cedula': forms.Select(attrs={
                'class': 'select2, form-control',
                'style': 'width: 100%'
            })
        }

    def save(self, commit=True):
        data = {}
        try:
            if self.is_valid():
                instance = super().save(commit=commit)
                data = instance.toJSON()
            else:
                data['error'] = self.errors
        except Exception as e:
            data['error'] = str(e)
        return data

class DoctorForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['autofocus'] = True

    class Meta:
        model = Doctor
        fields = ('nombre', 'apellido','cedula', 'tipo_cedula', 'especialidad')
        widgets = {
            'nombre': forms.TextInput(attrs={
                'placeholder': 'Ingrese el primer y segundo nombre', 
                'class': 'form-control'
            }),
            'apellido': forms.TextInput(attrs={
                'placeholder': 'Ingrese el primer y segundo apellido', 
                'class': 'form-control'
            }),
            'cedula': forms.TextInput(attrs={
                'placeholder': 'Ingrese un número de cedula', 
                'class': 'form-control'
            }),
            'especialidad': forms.Select(attrs={
                'class': 'select2 form-control',
                'style': 'width: 100%'
            }),
            'tipo_cedula': forms.Select(attrs={
                'class': 'form-control',
            })
        }

    def save(self, commit=True):
        data = {}
        try:
            if self.is_valid():
                instance = super().save(commit=commit)
                data = instance.toJSON()
            else:
                data['error'] = self.errors
        except Exception as e:
            data['error'] = str(e)
        return data
    
class CitaForm(ModelForm):
    hora = forms.TimeField(
        input_formats=['%I:%M %p', '%H:%M'],
        widget=forms.TimeInput(
            format='%I:%M %p',
            attrs={
                'class': 'form-control datetimepicker-input',
                'id': 'hora',
                'type': 'text',
                'data-target': '#hora',
                'data-toggle': 'datetimepicker',
                'placeholder': 'Ingrese la hora (ej: 02:00 PM)',
                'autocomplete': 'off'
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if args and args[0]:
            print(f"Raw hora value from POST: {args[0].get('hora')}")

    class Meta:
        model = Cita
        fields = '__all__'
        widgets = {
            'paciente': forms.Select(attrs={
                'class': 'select2 form-control',
            }),
            'doctor': forms.Select(attrs={
                'class': 'select2 form-control',
            }),
            'fecha': forms.DateInput(
                format='%Y-%m-%d', 
                attrs={
                    'class': 'form-control border-right-0 datetimepicker-input',
                    'id': 'fecha',
                    'value': datetime.now().strftime('%Y-%m-%d'),
                    'data-target': '#fecha',
                    'data-toggle': 'datetimepicker',
                }
            ),
            'observaciones': forms.Textarea(attrs={
                'class': 'form-control',
                'required': False,
                'rows': '2',
                'placeholder': 'Ingrese una observación',
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        print(f"Clean method - all cleaned_data: {cleaned_data}")
        print(f"Raw data before cleaning: {self.data}")
        return cleaned_data

    def save(self, commit=True):
        data = {}
        print(f"Save method - form errors: {self.errors}")
        print(f"Save method - cleaned_data: {self.cleaned_data}")
        
        try:
            if self.is_valid():
                instance = super().save(commit=commit)
                data = instance.toJSON()
            else:
                data['error'] = self.errors
        except Exception as e:
            data['error'] = str(e)
        return data
 


