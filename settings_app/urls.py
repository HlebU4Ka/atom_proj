from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Определение информации для документации API
api_info = openapi.Info(
    title="API",
    default_version='v1',
    description="Описание",
    terms_of_service="https://www.settings_app.com/terms/",
    contact=openapi.Contact(email="contact@yourapp.com"),
    license=openapi.License(name="Ваша лицензия"),
)

# Настройка для генерации схемы API
schema_view = get_schema_view(
    api_info,
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# Определение основных URL-маршрутов
urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('api/users/', include('users.urls')),
    path('api/habits/', include('habits.urls')),

    # Главная страница Swagger UI для интерактивной документации
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
