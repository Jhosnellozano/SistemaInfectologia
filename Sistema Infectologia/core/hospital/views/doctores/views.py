from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView

from core.hospital.forms import DoctorForm
from core.hospital.models import Doctor

class DoctorListView(LoginRequiredMixin, ListView):
    template_name = 'doctores/listado.html'
    model = Doctor

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            #Obtenemos la acción
            action = request.POST['action']
            if action == 'search':
                data = []
                for i in self.model.objects.all():
                    data.append(i.toJSON())
            
            elif action == 'delete':
                # Si ocurre algun error el proceso no se realizara
                with transaction.atomic():
                    get_id = request.POST['id']
                    #Verificar que exista el paciente
                    instance = get_object_or_404(self.model, id=int(get_id))
                    instance.delete()

            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Doctores'
        context['create_url'] = reverse_lazy('hospital:doctor_crear')
        context['list_url'] = reverse_lazy('hospital:doctor_listado')
        return context

class DoctorCreateView(LoginRequiredMixin, CreateView):
    model = Doctor
    form_class = DoctorForm
    template_name = 'doctores/crear.html'
    success_url = reverse_lazy('hospital:doctor_listado')

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Agregar Doctor'
        context['entity'] = 'Doctores'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context

class DoctorUpdateView(LoginRequiredMixin, UpdateView):
    model = Doctor
    form_class = DoctorForm
    template_name = 'doctores/crear.html'
    success_url = reverse_lazy('hospital:doctor_listado')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Doctor'
        context['entity'] = 'Doctores'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context
