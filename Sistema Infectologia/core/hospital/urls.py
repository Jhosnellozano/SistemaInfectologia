from django.urls import path
from .views.pacientes.views import PacienteListView, PacienteCreateView, PacienteUpdateView
from .views.doctores.views import DoctorListView, DoctorCreateView, DoctorUpdateView
from .views.citas.views import CitaListView, CitaCreateView, CitaUpdateView

app_name = 'hospital'

urlpatterns = [
    # pacientes
    path('paciente/listado/', PacienteListView.as_view(), name='paciente_listado'),
    path('paciente/crear/', PacienteCreateView.as_view(), name='paciente_crear'),
    path('paciente/editar/<int:pk>/', PacienteUpdateView.as_view(), name='paciente_editar'),
    # doctores
    path('doctor/listado/', DoctorListView.as_view(), name='doctor_listado'),
    path('doctor/crear/', DoctorCreateView.as_view(), name='doctor_crear'),
    path('doctor/editar/<int:pk>/', DoctorUpdateView.as_view(), name='doctor_editar'),
    # citas
    path('cita/listado/', CitaListView.as_view(), name='cita_listado'),
    path('cita/crear/', CitaCreateView.as_view(), name='cita_crear'),
    path('cita/editar/<int:pk>/', CitaUpdateView.as_view(), name='cita_editar'),
]
