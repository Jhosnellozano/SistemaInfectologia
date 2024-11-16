from django.urls import path
from .views import *

app_name = 'usuario'

urlpatterns = [
    # user
    path('listado/', UsuarioListView.as_view(), name='listado'),
    path('crear/', UsuarioCreateView.as_view(), name='crear'),
    path('editar/<int:pk>/', UsuarioUpdateView.as_view(), name='editar'),
    #path('add/', UserCreateView.as_view(), name='user_create'),
    # path('update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
    # path('delete/<int:pk>/', UserDeleteView.as_view(), name='user_delete'),
]
