from django.urls import path
from core.chat.consumers import PrivateChatConsumer

websocket_urlpatterns = [
    path('wss/<int:id>/', PrivateChatConsumer.as_asgi()),
]