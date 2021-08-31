

import os
from channels.routing import URLRouter, ProtocolTypeRouter
from channels.security.websocket import AllowedHostsOriginValidator
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from .routing import ws_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CHANNELS.settings')

application = ProtocolTypeRouter({
    'websocket': AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                ws_application
            )
        )
    )
})   
