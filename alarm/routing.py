from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r"ws/alarm/(?P<user_id>\w+)/$", consumers.AlarmConsumer.as_asgi()),
]
