from django.urls import path

from core.login.views import *

app_name = 'login'

urlpatterns = [
    path('', LoginFormView.as_view(), name='iniciar_sesion'),
    path('cerrar_sesion/', LogoutView.as_view(), name='cerrar_sesion'),
]
