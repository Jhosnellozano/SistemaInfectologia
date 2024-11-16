from django.urls import path
from core.chat.views import *

app_name = 'chat'

urlpatterns = [
    path('sala/', SalaListView.as_view(), name='sala'),
    path('usuario/', ChatUserListView.as_view(), name='usuario'),
]