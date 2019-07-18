from django.urls import path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from .views import HealthCheckViewSet

app_name = 'api'

list_actions = {'get': 'list'}

schema_view = get_schema_view(
    openapi.Info(
        title='Work at Olist API',
        default_version='v1',
        description='Work at Olist',
        contact=openapi.Contact(email='lucasinfologos@gmail.com'),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('health-check/', HealthCheckViewSet.as_view(list_actions), name='health_check'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(
        r'^docs(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json',
    ),
]
