from django.urls import path
from channels.routing import URLRouter
from chat.consumers import *

ws_application=[
    path("ws/chat/",ChatConsumer.as_asgi())
]