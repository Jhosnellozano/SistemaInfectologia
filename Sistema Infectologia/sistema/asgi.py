import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sistema.settings')

django_asgi_app = get_asgi_application()

from django.urls import path
from core.chat.consumers import PrivateChatConsumer

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter([
                path('ws/<int:id>/', PrivateChatConsumer.as_asgi()),
                ])
        )
    ),
})
#application = get_asgi_application()
# application = ProtocolTypeRouter({
#     # Django's ASGI application to handle traditional HTTP requests
#     "http": django_asgi_app,

#     # WebSocket chat handler
#     "websocket": AllowedHostsOriginValidator(
#         AuthMiddlewareStack(
#             URLRouter([
#                 path('ws/<int:id>/', PrivateChatConsumer.as_asgi()),
#             ])
#         )
#     ),
# })
# application = ProtocolTypeRouter({
#     # Django's ASGI application to handle traditional HTTP requests
#     "http": django_asgi_app,
#     'websocket': AuthMiddlewareStack(
#         URLRouter([
#             path('ws/<int:id>/', PrivateChatConsumer.as_asgi()),
#         ])
#     )
# })
