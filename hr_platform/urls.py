from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response

class BrowsableTokenAuth(ObtainAuthToken):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    def get(self, request, *args, **kwargs):
        return Response({'info': 'Введите username и password в форму ниже для получения токена'})


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('resumes.urls')),
    path('api-token-auth/', BrowsableTokenAuth.as_view(), name='api_token_auth'),
]
