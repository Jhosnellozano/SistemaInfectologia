import json
from django.utils.timesince import timesince
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView
from core.chat.models import *
from core.usuarios.models import Usuario
# Create your views here.

class SalaListView(ListView):   
    model = Sala

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            print('ACTION: ', action)
            if action == 'create_private_room':
                message_list = []
                user = Usuario.objects.values('username', 'id').get(id=request.POST['id'])
                username = user['username']
                name = f'{self.request.user}-{username}'
                usuario_actual = request.user
                sala_exist = Sala.objects.filter(usuario_sala__usuario=usuario_actual).filter(usuario_sala__usuario=user['id']).first()
                if sala_exist:
                    print('SI EXISTE LA SALA')
                    message = Mensaje.objects.filter(sala_id=sala_exist.id).order_by('-id')
                    count = message.count()
                    for m in message[0:20]:
                        item = {
                            'body': m.contenido,
                            'date_joined': timesince(m.fecha),
                            'first_user': m.usuario_id,
                            'second_user': usuario_actual.id,
                            'message_id': m.id,
                            'editado': m.editado
                        }
                        message_list.append(item)
                    return JsonResponse({'sala_id': sala_exist.id, 'count': count, 'message_list': message_list}, safe=False)
                    
                else:
                    print('NO EXISTE')
                    sala = Sala.objects.create(
                        nombre=name,
                        tipo_sala='PRIVADA'
                    )
                    users = [{'user': usuario_actual.id}, {'user': user['id']}]
                    for i in users:
                        Usuario_sala.objects.create(
                            usuario_id=int(i['user']),
                            sala_id=int(sala.id)
                    )    
                    return JsonResponse({'sala_id': sala.id}, safe=False)               
                
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

class ChatUserListView(ListView):   
    model = Usuario

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):        
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'load_user':
                data = []
                users = Usuario.objects.exclude(id=self.request.user.id)                    
                for i in users:                    
                    user = {
                        'id': i.id,
                        'full_name': i.get_full_name(),
                    }
                    data.append(user)
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)
