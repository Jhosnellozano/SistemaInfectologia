from django.contrib import admin
from django.conf import settings   
from django.conf.urls.static import static 
from django.urls import path, include
from django.views.generic import RedirectView
# handler404 = page_not_found404

urlpatterns = [
    path('', include('core.login.urls')),
    path('inicio/', include('core.inicio.urls')),
    path('admin/', admin.site.urls),
    path('hospital/', include('core.hospital.urls')),
    path('usuario/', include('core.usuarios.urls')),
    path('chat/', include('core.chat.urls')),
]
#agregaros al  urlpatterns la url de las imagenes
#if settings.DEBUG:
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)