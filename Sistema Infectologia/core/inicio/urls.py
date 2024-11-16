from django.urls import path
from core.inicio import views


app_name = 'dashboard'

urlpatterns = [
   path('inicio/', views.IndexView.as_view(), name="inicio"),
]
