from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView

from core.hospital.forms import CitaForm
from core.hospital.models import Cita

class CitaListView(LoginRequiredMixin, ListView):
    template_name = 'citas/listado.html'
    model = Cita

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
        context['title'] = 'Listado de Citas'
        context['create_url'] = reverse_lazy('hospital:cita_crear')
        context['list_url'] = reverse_lazy('hospital:cita_listado')
        return context

class CitaCreateView(LoginRequiredMixin, CreateView):
    model = Cita
    form_class = CitaForm
    template_name = 'citas/crear.html'
    success_url = reverse_lazy('hospital:cita_listado')

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                with transaction.atomic():
                    form = self.get_form()
                    data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Agregar Cita'
        context['entity'] = 'Citas'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context

class CitaUpdateView(LoginRequiredMixin, UpdateView):
    model = Cita
    form_class = CitaForm
    template_name = 'citas/crear.html'
    success_url = reverse_lazy('hospital:cita_listado')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                with transaction.atomic():
                    form = self.get_form()
                    data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Cita'
        context['entity'] = 'Citas'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context
