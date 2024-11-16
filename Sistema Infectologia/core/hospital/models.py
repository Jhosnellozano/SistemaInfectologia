from django.db import models
from datetime import date, timezone
from django.forms import model_to_dict
#from core.usuarios.models import Usuario

# -----------------------------------------------------

SEXO_CHOICES = [
    ("M", 'Masculino'),
    ("F", 'Femenino'),
]

TIPO_CEDULA_CHOICES = [
    ("V", 'Venezolano'),
    ("E", 'Extranjero'),
]

ESPECIALIDAD_CHOICES = [
    ("Medicina General", "Medicina General"),
    ("Pediatría", "Pediatría"),
    ("Ginecología", "Ginecología"),
    ("Traumatología", "Traumatología"),
    ("Dermatología", "Dermatología"),
    ("Oftalmología", "Oftalmología"),
    ("Odontología", "Odontología"),
    ("Psiquiatría", "Psiquiatría"),
    ("Cardiología", "Cardiología"),
]

class Paciente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    cedula = models.PositiveIntegerField(unique=True)
    fecha_nacimiento = models.DateField()
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    tipo_cedula = models.CharField(max_length=1, choices=TIPO_CEDULA_CHOICES, default=TIPO_CEDULA_CHOICES[0][0])
    direccion = models.CharField(max_length=200, null=True, blank=True)
    telefono = models.CharField(max_length=15)
    
    def __str__(self):
        return f"{self.full_name()} / {self.cedula}"
    
    def full_name(self):
        return f"{self.nombre} {self.apellido}"
    
    def calcular_edad(self):
        today = date.today()
        age = today.year - self.fecha_nacimiento.year - ((today.month, today.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day))
        return age
    
    def toJSON(self):
        item = model_to_dict(self)
        item['full_name'] = self.full_name()
        item['edad'] = self.calcular_edad()
        item['fecha_nacimiento'] = self.fecha_nacimiento.strftime('%Y-%m-%d')
        item['sexo'] = {'value': self.sexo, 'label': self.get_sexo_display()}
        item['tipo_cedula'] = {'value': self.tipo_cedula, 'label': self.get_tipo_cedula_display()}
        return item

class Doctor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=50)
    tipo_cedula = models.CharField(max_length=1, choices=TIPO_CEDULA_CHOICES, default=TIPO_CEDULA_CHOICES[0][0])
    cedula = models.PositiveIntegerField(unique=True)
    especialidad = models.CharField(max_length=20, choices=ESPECIALIDAD_CHOICES)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)
    fecha_modificacion = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"{self.full_name()} / {self.cedula}"
    
    def full_name(self):
        return f"{self.nombre} {self.apellido}"

    def save(self, *args, **kwargs):
        # Aquí puedes realizar otras acciones antes de guardar el objeto
        super().save(*args, **kwargs)
    
    def toJSON(self):
        item = model_to_dict(self)
        item['full_name'] = self.full_name()
        item['tipo_cedula'] = {'value': self.tipo_cedula, 'label': self.get_tipo_cedula_display()}
        item['fecha_creacion'] = self.fecha_creacion.strftime('%Y-%m-%d')
        item['fecha_modificacion'] = self.fecha_modificacion.strftime('%Y-%m-%d')
        return item

class Cita(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE) 
    doctor = models.ForeignKey(Doctor, on_delete=models.PROTECT)
    fecha = models.DateField()
    hora = models.TimeField()
    observaciones = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"Cita: {self.id} - paciente: {self.paciente.nombre} - doctor: {self.doctor.nombre}"
    
    def toJSON(self):
        item = model_to_dict(self)
        item['paciente'] = self.paciente.toJSON()
        item['doctor'] = self.doctor.toJSON()
        item['fecha'] = self.fecha.strftime('%Y-%m-%d')
        item['hora'] = self.hora.strftime('%H:%M %p')
        return item

# class Estudiante(models.Model):
#     nombre = models.CharField(max_length=100)
#     # Otros campos del modelo Estudiante

#     def __str__(self):
#         return self.nombre

# class Notas(models.Model):
#     estudiante = models.ForeignKey(Estudiante, related_name='notas', on_delete=models.CASCADE)
#     matematica = models.CharField(max_length=500)
#     lengua = models.CharField(max_length=500)
#     ciencias_sociales = models.CharField(max_length=500)
#     ciencias_naturales = models.CharField(max_length=500)
#     deporte = models.CharField(max_length=500)
#     cultura = models.CharField(max_length=500)

#     def __str__(self):
#         return self.matematica

# class Publicacion(models.Model):
#     titulo = models.CharField(max_length=100)
#     contenido = models.TextField()
#     autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)

# class Representante(models.Model):
#     ci_representante = models.CharField(max_length=10)
#     nombre_representante = models.CharField(max_length=50)
#     estudiante = models.ForeignKey(Estudiante, related_name='representantes', on_delete=models.CASCADE)
#     telefono = models.CharField(max_length=20)

#     def __str__(self):
#         return f"{self.nombre_representante} (ID: {self.id})"

# class Docente(models.Model):
#     id_docente = models.AutoField(primary_key=True)
#     nombre = models.CharField(max_length=50)
#     apellido = models.CharField(max_length=50)
#     cedula = models.CharField(max_length=10)
#     codigo_salon = models.CharField(max_length=10)
#     codigo_materia = models.CharField(max_length=10)

#     def __str__(self):
#         return f"{self.nombre} {self.apellido} (ID: {self.id_docente})"

# def get_default_codigo_materia():
#     return timezone.now().strftime('%Y-%m-%d %H:%M:%S')

# class Salon(models.Model):
#     codigo_salon = models.CharField(max_length=10)
#     estudiante = models.ForeignKey(Estudiante, related_name='salones', on_delete=models.CASCADE)
#     docente = models.ForeignKey(Docente, on_delete=models.CASCADE)
#     codigo_materia = models.CharField(max_length=10, default=get_default_codigo_materia)

#     def __str__(self):
#         return f"Código de salón: {self.codigo_salon} - Materia: {self.codigo_materia}"
