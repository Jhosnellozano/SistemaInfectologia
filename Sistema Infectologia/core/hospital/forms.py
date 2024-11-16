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
        form = super()
        try:
            if form.is_valid():
                instance = form.save()
                data = instance.toJSON()
            else:
                data['error'] = form.errors
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
        form = super()
        try:
            if form.is_valid():
                instance = form.save()
                data = instance.toJSON()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data
    
class CitaForm(ModelForm):

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
                format='%Y-%m-%d', attrs={
                'class': 'form-control border-right-0 datetimepicker-input',
                'id': 'fecha',
                'value': datetime.now().strftime('%Y-%m-%d'),
                'data-target': '#fecha',
                'data-toggle': 'datetimepicker',
            }),
            'hora': forms.TimeInput(
                format='%H:%M',
                attrs={
                    'class': 'form-control border-right-0 datetimepicker-input',
                    'id': 'hora',
                    'data-target': '#hora',
                    'data-toggle': 'datetimepicker',
            }),
            'observaciones': forms.Textarea(attrs={
                'class': 'form-control',
                'required': False,
                'rows': '2',
                'placeholder': 'Ingrese una observación',
            }),
            
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                instance = form.save()
                data = instance.toJSON()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data
 


